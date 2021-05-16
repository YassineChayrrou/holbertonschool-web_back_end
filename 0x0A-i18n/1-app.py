#!/usr/bin/env python3
""" Python Flask Module """


from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Babel Config class"""

    LANGUAGES = ["en", "fr"]


app.config['BABEL_DEFAULT_LOCALE'] = Config.LANGUAGES[0]


@app.route("/")
def index():
    """Index page"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
