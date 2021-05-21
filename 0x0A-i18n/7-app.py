#!/usr/bin/env python3
""" Python Flask Module """


from flask import Flask, g, render_template, request
from flask_babel import Babel
from pytz import timezone


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
def before_request():
    """ sets user as flask global """
    user = get_user()
    if user:
        g.user = user


@app.route("/")
def index_view():
    """ Handle Home route """
    return render_template("7-index.html")


@babel.localeselector
def get_locale():
    """ returns best matching language from request """
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    user = getattr(g, 'user', None)
    if user is not None:
        user_locale = user.get('locale')
        if user_locale in Config.LANGUAGES:
            return user_locale
    return request.accept_languages.best_match(Config.LANGUAGES)


@babel.timezoneselector
def get_timezone() -> str:
    """ returns user timezone """
    try:
        URL_TIMEZONE = request.args.get('timezone')
        if URL_TIMEZONE:
            return timezone(URL_TIMEZONE)
        user = getattr(g, 'user', None)
        if user:
            user_timezone = user.get('timezone')
            return timezone(user_timezone)
    except pytz.exceptions.UnknownTimeZoneError:
        return timezone(Config.BABEL_DEFAULT_TIMEZONE)


if __name__ == "__main__":
    app.run(debug=True)
