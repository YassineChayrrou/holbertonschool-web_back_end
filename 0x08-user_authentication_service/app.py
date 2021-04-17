#!/usr/bin/env python3
""" Flask app module """


from flask import abort, Flask, jsonify, request
from auth import Auth


app = Flask(__name__)
auth = Auth()


@app.route("/", methods=['GET'])
def index():
    """
    index - returns json and the end point '/'
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'])
def users():
    """
    users - flask app implementation of user registration in auth module
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = auth.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"})
    return jsonify({
        "email": email,
        "message": "user created"
        })


@app.route("/sessions", methods=['POST'])
def login():
    """
    login - session setup and implementation in flask app end point /sessions
    """
    email = request.form.get('email')
    password = request.form.get('password')
    is_valid = auth.valid_login(email, password)
    if is_valid:
        session_id = auth.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie('session_id', session_id)
        return response
    else:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
