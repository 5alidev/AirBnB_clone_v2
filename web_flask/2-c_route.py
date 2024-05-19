#!/usr/bin/python3
"""
script that starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """
    Home route
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    HBNB route
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cIsFun(text):
    """
    display C followed by the value of the <text>
    """
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
