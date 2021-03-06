import os
import glob
import time
import requests
import json
import operator
import urllib.request
import engine
import db_helper
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


@app.route('/customers')
def render_customers_page():
    return render_template('customers.html')


@app.route('/results')
def render_results_page():
    rows = db_helper.fetch_rows()

    return render_template('results.html', rows=rows)


@app.route('/topics')
def render_topics_page():
    return render_template('topics.html')


@app.route('/complaints')
def render_complaints_page():
    return render_template('complaints.html')


@app.route('/report')
def render_report_page():
    return render_template('report.html')


@app.route('/dropzone')
def dropzoneview():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        for key, f in request.files.items():
            if key.startswith('file'):
                f.save(os.path.join('files', f.filename))

        engine.process()

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
