#!/usr/bin/env python3
"""This modules houses the declaration of a flask application
that uses babel to support multiple langiages"""
from flask import (
    Flask,
    render_template
)
from flask_babel import Babel   # type: ignore
from typing import List


class Config:
    """Configures a babel's to support multiple languages"""
    LANGUAGES: List[str] = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE: str = 'UTC'


app: Flask = Flask(__name__)
app.config.from_object(Config)
babel: Babel = Babel(app)


@app.route('/')
def index():
    """renders the content of the index to the webpage"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
