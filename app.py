from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world'

@app.route("/whoiam")
def me():
    name = "Noah"
    nationality = "Korean"

    return f"My name is {name}, and my nationality is {nationality}."