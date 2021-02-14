import os
import glob
import time
import requests
import json
import operator
import urllib.request
import engine
from flask import Flask, request, render_template, redirect, url_for, jsonify, make_response
from flask_dropzone import Dropzone
from flask_mysqldb import MySQL

app = Flask(__name__)

dropzone = Dropzone(app)

# Dropzone settings
app.config['DROPZONE_UPLOAD_MULTIPLE'] = True
app.config['DROPZONE_MAX_FILES'] = 10
app.config['DROPZONE_PARALLEL_UPLOADS'] = 10

app_path = os.path.dirname(os.path.realpath(__file__))
files = {}  

@app.route('/process/<filename>', methods=['GET'])
def singlefile(filename):
    result = engine.single_file(filename)
    return make_response(jsonify(result), 200)

@app.route('/process', methods=['POST'])
def process():
    result = engine.process()
    return make_response(jsonify(result), 200)

@app.route('/temp')
def temp():
    return render_template('temp.html')

@app.route('/dropzone')
def dropzoneview():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    status = "n/a"

    if request.method == 'POST':
        for key, f in request.files.items():
            if key.startswith('file'):
                f.save(os.path.join('files', f.filename))

        result = engine.process()
        print(result)
        status = "The audio files will be processed in the background"

    return render_template('index.html', status = status)

if __name__ == '__main__':
    app.run(debug=True)