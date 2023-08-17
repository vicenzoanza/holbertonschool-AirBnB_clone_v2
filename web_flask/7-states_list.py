#!/usr/bin/python3
"""List of states"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def app_teardown_appcontext(self):
    "Close the session after each request"
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    return render_template("7-states_list.html",
                           states=storage.all(State).values().order_by(State.name))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)