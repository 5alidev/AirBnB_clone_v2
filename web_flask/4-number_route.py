#!/usr/bin/python3
"""
script that starts a Flask web application
"""

from flask import Flask
app = Flask("__name__")


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
    display C, followed by the value of the <text>
    """
    return "C " + text.replace("_", " ")


@app.route('/python/', defaults={"text": "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonRoute(text):
    """
    display Python, followed by the value of the <text>
    """
    return "Python " + text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def ifNumber(n):
    """
    display <n> is a number only if n is an integer
    """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
