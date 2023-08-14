#!/usr/bin/python3
'''starts a script'''
from flask import Flask, abort


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    '''displays a message'''
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''displays a message'''
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    text_with_spaces = text.replace('_', ' ')
    return "c {}".format(text_with_spaces)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_p_text(text):
    text_with_spaces = text.replace('_', ' ')
    return "Python {}".format(text_with_spaces)

@app.route('/number/<n>', strict_slashes=False)
def is_num(n):
    try:
        n_int = int(n)
        if isinstance(n_int, int):
            return "{} is a number".format(n)
    except ValueError:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
