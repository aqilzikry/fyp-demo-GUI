import os
import glob
import time
import requests
import json
import urllib.request
from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_dropzone import Dropzone
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ccas_db'

dropzone = Dropzone(app)

URL = "http://127.0.0.1:7000"

app_path = os.path.dirname(os.path.realpath(__file__))
files = {}

@app.route('/uploads', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join('files', f.filename))

    #files.clear()
    #for file in os.listdir(os.path.join(app_path, 'files')):
    #    files[file] = time.ctime(os.path.getctime(os.path.join(app_path, 'files', file)))

    #with urllib.request.urlopen(URL) as url:
    #    data = json.loads(url.read().decode())

    #respond = requests.get(URL)
    respond = requests.get(URL + "/Demo_angry_malay.wav")
    print(respond)
    json_data = respond.json()
    json_data = json.dumps(json_data, indent=4)

    return render_template('index.html', files = files, data = json_data)

if __name__ == '__main__':
    app.run(debug=True)