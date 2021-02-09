import os
import glob
import time
from flask import Flask, request, render_template, redirect, url_for
from flask_dropzone import Dropzone

app = Flask(__name__)

dropzone = Dropzone(app)

app_path = os.path.dirname(os.path.realpath(__file__))
files = {}

@app.route('/uploads', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join('files', f.filename))

    files.clear()
    for file in os.listdir(os.path.join(app_path, 'files')):
        files[file] = time.ctime(os.path.getctime(os.path.join(app_path, 'files', file)))

    return render_template('index.html', files = files)

if __name__ == '__main__':
    app.run(debug=True)