# 0x08. User authentication service

In this project we do a user authentication based on modules stored on database (sqlite3) using sqlalchemy as our Object Relational Mapper and creating our own authentication system for storing and retrieving data from DB and so forth.

**Note:**
In industry we usually use tested, secure and maintained authentication systems rather then making our own, this would be faster for development and more secure for our client, and example of that would be [Flask-User](https://flask-user.readthedocs.io/en/latest/).<br>
This project is concerned about understanding the intricacies of user authentication so we try to build it from scratch to better develop our comprehension.

## Resources:

**Read or watch:**
- <a href="https://flask.palletsprojects.com/en/1.1.x/quickstart/" target="_blank">Flask documentation</a>
- <a href="https://requests.kennethreitz.org/en/master/user/quickstart/" target="_blank">Request module</a>
- <a href="https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html" target="_blank">HTTP status codes</a>

## Learning Objectives:

At the end of this project, we are expected to be able to explain to anyone, without the help of Google:

- How to declare API routes in a Flask app
- How to get and set cookies
- How to retrieve request form data
- How to return various HTTP status codes

# setup:

we need to install bcrypt and sqlalchemy
```
pip3 install bcrypt
```
```
pip3 install SQLAlchemy
```
