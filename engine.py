import speech_recognition as sr
import pickle
import os
import glob
import malaya as m
import json
import operator
import mysql.connector
from flask import Flask
from monkeylearn import MonkeyLearn
from emotion_recog import extract_feature
from celery import Celery

engine = Flask(__name__)

# Set up celery client
client = Celery(engine.name, backend="redis://localhost:6379/0", broker="redis://localhost:6379/0")

toReturn = {}

# initiate speech recognizer and set language (Malay: ms-MY, English: en-US)
r = sr.Recognizer()

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "ccas_db"
)

filename = ""
filelocation = ""
text = ""
lang = "ms-MY"

def recog_speech():
    # prepare audio for recognition
    speech = sr.AudioFile(filelocation)
    with speech as source:
        audio = r.record(source)

    # recognize speech and return result 
    global text
    text = r.recognize_google(audio, language=lang)

    return text

def recog_emotion():
    # load the saved model (after training)
    model = pickle.load(open("model/emotionrecog.model", "rb"))

    # extract features and reshape it
    features = extract_feature(filelocation, mfcc=True, chroma=True, mel=True).reshape(1, -1)

    # predict emotion
    result = model.predict_proba(features)

    # add result to dict
    emotion = {'angry' : result[0][0], 'happy' : result[0][1], 'neutral' : result[0][2]}
    print(emotion)
    
    return emotion

def analyse_sentiment():
    # use different model for different language
    if lang == "ms-MY":
        # load sentiment model from malaya and run on text
        multinomial = m.sentiment.multinomial()
        sentiment = multinomial.predict_proba([text])     
    elif lang == "en-US":
        # private MonkeyLearn API key, do not distribute
        ml = MonkeyLearn('ff1cfdaf494ec22525462f2749bdafd87a582890')
        data = [text]
        model_id = 'cl_pi3C7JiL'
        result = ml.classifiers.classify(model_id, data).body

        # retrieve sentiment label from dictionary
        sentiment = result[0]["classifications"][0]["tag_name"], str(result[0]["classifications"][0]["confidence"])
    
    # add result to dict
    return sentiment[0]

def detect_topic():
    # load transformer model 'alxlnet' from malaya
    model = m.zero_shot.classification.transformer(model = 'alxlnet')

    # run prediction on labels
    result = model.predict_proba([text], labels = ['view bill', 'bekalan elektrik', 'bantuan'])
    
    # sort labels by likeliness
    sorted_result = sorted(result[0].items(), key=lambda x: x[1], reverse=True)

    for i in range(0, len(sorted_result)):
        sorted_result[i] = list(sorted_result[i])
        sorted_result[i][1] = sorted_result[i][1].item()

    # add result to dict
    return dict(sorted_result)

@client.task
def iterate_files():
    for file in glob.glob("files/*.wav"):
        global filename
        filename = os.path.basename(file)
        global filelocation
        filelocation = file
        toReturn[filename] = ({'audio' : filename})
        toReturn[filename] = ({'speech' : recog_speech()})
        toReturn[filename].update({'emotion' : recog_emotion()})
        toReturn[filename].update({'sentiment' : analyse_sentiment()})
        toReturn[filename].update({'topic' : detect_topic()})
        save_to_db(filename)
        os.remove(file)

    return toReturn

def process():
    #toReturn = iterate_files()

    iterate_files.apply_async()

    #return toReturn
    return "Success"

def main():
    toReturn = iterate_files()

    return toReturn

def single_file(toProcess):
    for file in glob.glob("files/*.wav"):
        if os.path.basename(file) == toProcess:
            global filename
            filename = os.path.basename(file)
            global filelocation
            filelocation = file
            toReturn[filename] = ({'speech' : recog_speech()})
            toReturn[filename].update({'emotion' : recog_emotion()})
            toReturn[filename].update({'sentiment' : analyse_sentiment()})
            toReturn[filename].update({'topic' : detect_topic()})
            return toReturn

def save_to_db(currentFile):
    topics = json.dumps(toReturn[currentFile]['topic'])

    emotion = max(toReturn[currentFile]['emotion'].items(), key=operator.itemgetter(1))[0]
    emotion_prob = float(toReturn[currentFile]['emotion'][emotion])
    
    sentiment = max(toReturn[currentFile]['sentiment'].items(), key=operator.itemgetter(1))[0]
    sentiment_prob = float(toReturn[currentFile]['sentiment'][sentiment])

    cur = mydb.cursor()
    cur.execute("INSERT INTO calls(operator_id, audio, emotion, emotion_prob, sentiment, sentiment_prob, topics, cust_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", ("1", filename, emotion, emotion_prob, sentiment, sentiment_prob, topics, "1"))
    mydb.commit()
    cur.close()
    print(currentFile + ' success')

if __name__ == "__main__":
    main()