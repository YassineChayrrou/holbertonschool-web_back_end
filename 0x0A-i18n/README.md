# 0x0A. i18n

Internationalization and localization sometimes shortened to I18N.
I18N presents the design and development of a product, application or document content that enables easy localization for target audience that vary in culture, region, or language.


## Resources:

**Read or watch:**
- <a href="https://flask-babel.tkte.ch/" target="_blank">Flask-Babel</a>
- <a href="https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n" target="_blank">Flask i18n tutorial</a>
- <a href="http://pytz.sourceforge.net/" target="_blank">pytz</a>

## Learning Objectives:


- Learn how to parametrize Flask templates to display different languages
- Learn how to infer the correct locale based on URL parameters, user settings or request headers
- Learn how to localize timestamps

## Extras:

requirements:
- flask and flask_babel installation

```
pip3 install flask
pip3 install flask_babel
```
- compile translation through babel
    - create babel.cfg file and copy paste this code into it
    ```
    [python: **.py]
    [jinja2: **/templates/**.html]
    extensions=jinja2.ext.autoescape,jinja2.ext.with_
    ```
    - Initialize translations
    ```
    pybabel extract -F babel.cfg -o messages.pot .
    ```
    ```
    pybabel init -i messages.pot -d translations -l en
    pybabel init -i messages.pot -d translations -l fr
    ```
    - after setting up message.pot files to command specific translations you can compile using this command
    ```
    pybabel compile -d translations
    ```

## Author:

Yassine Chayrrou
