import os
from flask import Flask, request, render_template
from flask_dropzone import Dropzone

app = Flask(__name__)

dropzone = Dropzone(app)

@app.route('/uploads', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join('files', f.filename))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)