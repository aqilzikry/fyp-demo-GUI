import os
import glob
import time
import requests
import json
import operator
import urllib.request
from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_dropzone import Dropzone
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ccas_db'

mysql = MySQL(app)
dropzone = Dropzone(app)

URL = "http://127.0.0.1:7000"

app_path = os.path.dirname(os.path.realpath(__file__))
files = {}

@app.route('/uploads', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join('files', f.filename))

    #respond = requests.get(URL)
    respond = requests.get(URL + "/process/Demo_angry_malay.wav")
    print(respond)
    json_data = respond.json()
    dumped_json_data = json.dumps(json_data, indent=4)

    res = next(iter(json_data)) 
    topics = json.dumps(json_data[res]['topic'])

    emotion = max(json_data[res]['emotion'].items(), key=operator.itemgetter(1))[0]
    emotion_prob = json_data[res]['emotion'][emotion]
    
    sentiment = max(json_data[res]['sentiment'].items(), key=operator.itemgetter(1))[0]
    sentiment_prob = json_data[res]['sentiment'][sentiment]

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO calls(operator_id, emotion, emotion_prob, sentiment, sentiment_prob, topics, cust_id) VALUES (%s, %s, %s, %s, %s, %s, %s)", ("1", emotion, emotion_prob, sentiment, sentiment_prob, topics, "1"))
    mysql.connection.commit()
    cur.close()

    return render_template('index.html', files = files, data = dumped_json_data)

if __name__ == '__main__':
    app.run(debug=True)