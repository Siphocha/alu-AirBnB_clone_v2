#!/usr/bin/python3
"""testing and running flask server"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    """prints out when ran"""
    return "Hello HBNB!"


if __name__ == "__main__":
    """Define which port application runs from"""
    app.run(host="0.0.0.0", port="5000")
