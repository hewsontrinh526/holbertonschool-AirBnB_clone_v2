#!/usr/bin/python3
"""
A script that starts a Flask web application with different routes like '/',
'/hbnb', '/c/<text>', '/python/<text>' and '/number/<n>'
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Displays a Hello string
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays a HBNB string
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Displays a C followed by the value of the text variable
    """
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Displays a Python followed by the value of the text variable
    """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Displays n is a number only if n is an integer
    """
    if type(n) is int:
        return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
