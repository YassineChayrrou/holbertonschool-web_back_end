#!/usr/bin/env python3
""" End-to-end integeration test module """


from flask import json
import requests


URL = 'http://0.0.0.0:5000'

def register_user(email: str, password: str) -> None:
    """
    Test for /users end-point
    checks if new user is registered 
    """
    payload = {
            'email': email,
            'password': password
            }
    req = requests.post(URL + '/users', data=payload)
    assert req.status_code == 200


def log_in_wrong_password(email: str, password: str) -> None:
    """
    Test wrong login on /sessions end-point
    """
    payload = {
            'email': email,
            'password': password
            }
    req = requests.post(URL + '/sessions', data=payload)
    assert req.status_code == 401

def log_in(email: str, password: str) -> str:
    """
    Test successful login on /sessions end-point
    """
    payload = {
            'email': email,
            'password': password
            }
    req = requests.post(URL + '/sessions', data=payload)
    assert req.status_code == 200 
    return req.cookies.get('session_id')

def profile_unlogged() -> None:
    """
    Test user profile without session_id on '/profile' end-point
    """
    req = requests.get(URL + '/profile')
    assert req.status_code == 403

def profile_logged(session_id: str) -> None:
    """
    Test Session active status after initial log in using session_id
    """
    session_cookie = {'session_id': session_id}
    req = requests.get(URL + '/profile', cookies=session_cookie)
    assert req.status_code == 200

def log_out(session_id: str) -> None:
    """
    Test Session_id deleted and user is logged out on '/sessions' end-point
    """
    session_cookie = {'session_id': session_id}
    req = requests.delete(URL + '/sessions', cookies=session_cookie)
    assert req.status_code == 200

def reset_password_token(email: str) -> str:
    """
    Test if new reset_token is generated on '/reset_password' end-point
    """
    payload = {
            'email': email
            }
    req = requests.post(URL + '/reset_password', data=payload)
    assert req.status_code == 200
    reset_token = json.loads(req.content).get('reset_token')
    return reset_token

def update_password(email: str, reset_token: str, new_password: str) -> None:
    """
    Test user update password on '/reset_password' end-point
    """
    payload = {
            'email': email,
            'reset_token': reset_token,
            'new_password': new_password
            }
    req = requests.put(URL + '/reset_password', data=payload)
    assert req.status_code == 200




EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
