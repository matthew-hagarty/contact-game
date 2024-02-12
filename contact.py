from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
@app.route("/<name>")
def hello_world(name=None):
    return render_template('contact.html', name=name)
