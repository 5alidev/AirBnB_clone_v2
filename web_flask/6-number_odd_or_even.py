#!/usr/bin/python3
"""
script that starts a Flask web application
"""

from flask import Flask, render_template

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


@app.route('/number_template/<int:n>', strict_slashes=False)
def numTemplate(n):
    """
    display a HTML page only if n is an integer
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def oddOrEven(n):
    """
    display if n is odd or even
    """
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', n=n, nm='even')
    elif n % 2 == 1:
        return render_template('6-number_odd_or_even.html', n=n, nm='odd')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
