import flask
import engine
import json
from flask import jsonify, make_response

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    result = engine.main()
    return make_response(jsonify(result), 200)

app.run(host='127.0.0.1', port=7000)