#!/usr/bin/env python3
""" Python Flask Module """


from flask import Flask, g, render_template, request
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """ Babel Config class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object("5-app.Config")
babel = Babel(app)


def get_user():
    """gets user from users"""
    id = request.args.get('login_as')
    if id is None or int(id) not in users:
        return None
    return users.get(int(id))


@app.before_request
def before_request_function():
    user = get_user()
    if user:
        g.user = user
    print(user)


@app.route("/")
def index_view():
    """ Handle Home route """
    return render_template("5-index.html")


@babel.localeselector
def get_locale():
    """ returns best matching language from request """
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(Config.LANGUAGES)


if __name__ == "__main__":
    app.run(debug=True)
    print(get_user())
