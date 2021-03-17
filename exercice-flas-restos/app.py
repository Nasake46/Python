from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/settings")
def settings():
    return 'settings'

@app.route("/")
def slash():
    return 'salut'

@app.route("/date/<format>")
def date(format):
    return datetime.now().strftime(format) + "\n"

