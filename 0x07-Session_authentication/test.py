#!/usr/bin/env python3
"""Test for session db storage module"""


from flask import Flask, request
from api.v1.auth.session_auth import SessionAuth
from models.user import User
from api.v1.auth.session_db_auth import SessionDBAuth

""" Create a user test """
user_email = "bobsession@hbtn.io"
user_clear_pwd = "fake pwd"

user = User()
user.email = user_email
user.password = user_clear_pwd
user.save()

""" Create a session ID """
sa = SessionDBAuth()
session_id = sa.create_session(user.id)
print("User with ID: {} has a Session ID: {}".format(user.id, session_id))
print("--------------------------------------------------------------")
""" User ID For Session ID """
user_id = sa.user_id_for_session_id(session_id)
print(f"Session with ID: {session_id} has a User ID: {user_id}")


""" Create a Flask app """
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def root_path():
    """ Root path
    """
    request_user = sa.destroy_session(request)
    if request_user is None:
        return "No session found\n"
    return "Result: {}\n".format(request_user)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
