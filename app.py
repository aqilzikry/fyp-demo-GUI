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

#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = ''
#app.config['MYSQL_DB'] = 'ccas_db'

#mysql = MySQL(app)
dropzone = Dropzone(app)

app_path = os.path.dirname(os.path.realpath(__file__))
files = {}

@app.route('/', methods=['GET'])
def home():
    return redirect(url_for('upload'))    

@app.route('/process/<filename>', methods=['GET'])
def singlefile(filename):
    result = engine.single_file(filename)
    return make_response(jsonify(result), 200)

@app.route('/process', methods=['POST'])
def process():
    result = engine.process()
    return make_response(jsonify(result), 200)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join('files', f.filename))
        result = engine.process()

        return render_template('index.html', files = result)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)