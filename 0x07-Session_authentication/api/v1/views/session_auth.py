#!/usr/bin/env python3
""" SessionAuth view module
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ Login session view
    """
    email = request.form.get('email')
    if not email:
        return jsonify({'error': 'email missing'}), 400
    password = request.form.get('password')
    if not password:
        return jsonify({'error': 'password missing'}), 400
    users = User.search({'email': email})
    if not users:
        return jsonify({'error': 'no user found for this email'}), 404
    current_user = users[0]
    pwd_validation = current_user.is_valid_password(password)
    if pwd_validation is False:
        return jsonify({'error': 'wrong password'}), 401
    else:
        from api.v1.app import auth
        session_id = auth.create_session(current_user.id)
        response = jsonify(current_user.to_json())
        response.set_cookie(getenv('SESSION_NAME'), str(session_id))
        print(session_id)
        return response


@app_views.route(
        '/auth_session/logout',
        methods=['DELETE'],
        strict_slashes=False
        )
def logout():
    """ Logout from session
    """
    from api.v1.app import auth
    session_status = auth.destroy_session(request)
    if not session_status:
        return False, abort(404)
    return jsonify({})
