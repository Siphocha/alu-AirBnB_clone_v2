#!/usr/bin/python3
"""testing and running flask server"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    """prints out when ran"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """check returning"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_text(text):
    """tests to see if text display works"""
    return "C " + text.replace("_", " ")


@app.route("/python/<text>",
           strict_slashes=False,
           defaults={'text': 'is cool'})
def display_python(text):
    """Same function as above but using Python text"""
    return "Python " + text.replace('_', ' ')


if __name__ == '__main__':
    """Define which port application runs from"""
    app.run(host="0.0.0.0", port="5000")
