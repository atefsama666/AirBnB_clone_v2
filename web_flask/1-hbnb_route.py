#!/usr/bin/python3
"""Python Module"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def helloHbnb():
    """Python Method"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Python Method"""
    return 'HBNB'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
