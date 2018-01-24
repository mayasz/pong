#! /usr/bin/python
# pong.py

# servers js (p5) files for pong game

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/pong')
def pong():
    return 'Hello, pong!'


if __name__ == "__main__":
    app.run(host= '0.0.0.0')