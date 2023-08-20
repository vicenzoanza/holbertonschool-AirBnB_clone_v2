#!/usr/bin/python3
""" Write a script that starts a Flask web """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_ab():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_ab1():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def hello_ab2(text):
    text = text.replace("_", " ")
    return f"C {text}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_ab3(text):
    text = text.replace('_', ' ')
    return f"Python {text}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    