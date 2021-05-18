#!/usr/bin/env python3
""" Python Flask Module """


from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ Babel Config class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object("1-app.Config")
babel = Babel(app)


@app.route("/")
def index_view():
    """ Handle Home route """
    return render_template("3-index.html")


@babel.localeselector
def get_locale():
    """ returns best matching language from request """
    return request.accept_languages.best_match(Config.LANGUAGES)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
