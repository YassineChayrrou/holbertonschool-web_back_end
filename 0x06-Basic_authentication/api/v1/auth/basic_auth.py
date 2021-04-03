#!/usr/bin/env python3
"""BasicAuth model"""


from .auth import Auth
from typing import TypeVar
from models.user import User
from models.base import DATA
from flask import jsonify
import base64
import binascii


class BasicAuth(Auth):
    """BasicAuth class
    """

    def __init__(self):
        pass

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Returns Base64 part of Authorization in header for Basic Auth"""
        if authorization_header is None:
            return None
        elif type(authorization_header) is not str:
            return None
        elif authorization_header[:6] != "Basic ":
            return None
        else:
            base64 = authorization_header.split(" ")[1]
            return base64

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """Returns decoded value of a Base64 string
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            base64_decode_bytes = base64.b64decode(base64_authorization_header)
            base64_decode_text = base64_decode_bytes.decode('ascii')
            return base64_decode_text
        except (binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> (str, str):
        """ Retruns user email and password from Base64 decoded value
        """
        if decoded_base64_authorization_header is None:
            return None, None
        elif type(decoded_base64_authorization_header) is not str:
            return None, None
        elif ":" not in decoded_base64_authorization_header:
            return None, None
        else:
            return tuple(decoded_base64_authorization_header.split(":", 1))

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """ Returns User instancebased on his email and password
        """
        if user_email is None or type(user_email) is not str:
            return None
        if user_pwd is None or type(user_pwd) is not str:
            return None
        if not DATA:
            return None
        users = User.search({"email": user_email})
        if len(users) < 1:
            return None
        current_user = users[0]
        password_validation = current_user.is_valid_password(user_pwd)
        if password_validation is True:
            return current_user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns current user instance if authorized
        """
        auth_value = self.authorization_header(request)
        b64_auth = self.extract_base64_authorization_header(auth_value)
        b64_auth_decoded = self.decode_base64_authorization_header(b64_auth)
        credentials = self.extract_user_credentials(b64_auth_decoded)
        usr = self.user_object_from_credentials(credentials[0], credentials[1])
        return usr
