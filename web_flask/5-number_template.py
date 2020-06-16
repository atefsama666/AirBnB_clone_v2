#!/usr/bin/python3
"""Python Module"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def helloHbnb():
    """Python Method"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Python Method"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cfunc(text):
    """Python Method"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """Python Method"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:number>', strict_slashes=False)
def number(number):
    """Python Method"""
    return '{} is a number'.format(number)


@app.route('/number_template/<int:number>', strict_slashes=False)
def numberHtml(number):
    """Python Method"""
    return render_template('5-number.html', number=number)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
