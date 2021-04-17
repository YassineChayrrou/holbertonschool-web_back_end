#!/usr/bin/env python3
""" Flask app module """


from flask import abort, Flask, jsonify, redirect, request, url_for
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


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
        user = AUTH.register_user(email, password)
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
    is_valid = AUTH.valid_login(email, password)
    if is_valid:
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie('session_id', session_id)
        return response
    else:
        abort(401)


@app.route("/sessions", methods=['DELETE'])
def logout():
    """
    logout - logout implementation destroys current user session
    """
    session_id = request.cookies.get('session_id')
    current_user = AUTH.get_user_from_session_id(session_id)
    if current_user:
        user_id = current_user.id
        AUTH.destroy_session(user_id)
        return redirect(url_for('index'))
    else:
        abort(403)


@app.route("/profile", methods=['GET'])
def profile():
    """
    profile - gets user profile based on session_id
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        email = user.email
        return jsonify({"email": email})
    else:
        abort(403)


@app.route("/reset_password", methods=['POST'])
def get_reset_password_token():
    """
    get_reset_password_token - resets password token flask implementation
    """
    email = request.form.get('email')
    try:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token}), 200
    except Exception as e:
        abort(403)


@app.route("/reset_password", methods=['PUT'])
def update_password():
    """
    update_password - updates users password
    """
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')

    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"})
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
