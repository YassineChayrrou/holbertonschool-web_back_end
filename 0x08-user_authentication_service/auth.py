#!/usr/bin/env python3
""" Auth module
    manages authentication related operations
    main imports:
        - bcrypt
    module name 'auth'
"""


import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """
    _hash_password - hashes passed argument
    Args:
        - password: str, text to hash
    Return:
        - hashed bytes string using bcrypt
    """
    password = password.encode()
    salt = bcrypt.gensalt()
    hashed_passwd = bcrypt.hashpw(password, salt)
    return hashed_passwd


def _generate_uuid() -> str:
    """
    _generate_uuid - generates a new UUID
    Args:
        - takes no arguments
    Return:
        - UUID string representation
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        register_user - registers user to database
        Args:
            - email: str, takes user email
            - password: str, takes user password
        Return:
            - User instance after registration
            - raise a ValueError if user already exists
        """
        try:
            status = self._db.find_user_by(email=email)
            if status:
                raise ValueError(f"User {email} already exists")
        except (AttributeError, NoResultFound):
            pass
        password = _hash_password(password)
        registered_user = self._db.add_user(email, password)
        return registered_user

    def valid_login(self, email: str, password: str) -> bool:
        """
        valid_login - check the validation of login credentials
        Args:
            - email: str, user email
            - password: str, user password
        Return:
            - True or False
        """
        if email and password:
            try:
                user = self._db.find_user_by(email=email)
                user_pwd = user.hashed_password
                password = bytes(password.encode())
                validation = bcrypt.checkpw(password, user_pwd)
                if validation:
                    return True
            except Exception as e:
                return False
        return False
