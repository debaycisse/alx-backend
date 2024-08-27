#!/usr/bin/env python3
"""This module houses the definition of an instance of flask application"""
from flask import (
    Flask,
    render_template
)


app: Flask = Flask(__name__)


@app.route('/')
def index():
    """Handles every request to the root's route"""
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run()
