#!/usr/bin/python3
""" Write a script that starts a Flask web """
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def ab():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def ab1():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def ab2(text):
    text = text.replace("_", " ")
    return f"C {text}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def ab3(text):
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def ab4(n):
    return f"{n} is a number"


@app.route('/number_template/<n>', strict_slashes=False)
def ab5(n):
    n = int(n)
    return render_template('5-number.html', n=n)
  

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
