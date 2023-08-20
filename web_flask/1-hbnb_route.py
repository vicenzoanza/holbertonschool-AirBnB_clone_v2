#!/usr/bin/python3
""" Write a script that starts a Flask web """
from flask import Flask


app = Flask(__name__)


@app.route('/')
def ab():
    return "Hello HBNB!"


@app.route('/hbnb')
def ab1():
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
