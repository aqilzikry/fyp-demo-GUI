import speech_recognition as sr
import pickle
import os
import glob
import malaya as m
import json
from monkeylearn import MonkeyLearn
from emotion_recog import extract_feature

toReturn = {}
# initiate speech recognizer and set language (Malay: ms-MY, English: en-US)
r = sr.Recognizer()

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

def iterate_files():
    for file in glob.glob("files/*.wav"):
        global filename
        filename = os.path.basename(file)
        global filelocation
        filelocation = file
        toReturn[filename] = ({'speech' : recog_speech()})
        toReturn[filename].update({'emotion' : recog_emotion()})
        toReturn[filename].update({'sentiment' : analyse_sentiment()})
        toReturn[filename].update({'topic' : detect_topic()})

    return toReturn

def main():
    toReturn = iterate_files()

    #text = recog_speech()

    # add result to dict
    #toReturn['speech'] = text

    # run emotion recognition
    #recog_emotion()    

    # run sentiment analysis
    #analyse_sentiment()

    # run topic classification
    #detect_topic()

    # dump dict to a json file
    #with open("sample.json", "w") as outfile:
    #    json.dump(toReturn, outfile)

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

if __name__ == "__main__":
    main()