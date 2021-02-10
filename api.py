import flask
import engine
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    result = dict(engine.main())
    print(type(result))
    return result

app.run()