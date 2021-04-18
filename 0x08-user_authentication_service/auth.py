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
        try:
            user = self._db.find_user_by(email=email)
            if not user:
                return False
            password = password.encode('utf-8')
            validation = bcrypt.checkpw(password, user.hashed_password)
            if validation:
                return True
            return False
        except Exception as e:
            return False

    def create_session(self, email: str):
        """
        create_session - creates new session and store it in DB
        Args:
            - email: str, user email
        Return:
            - session ID as string
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        session_id = _generate_uuid()
        user.session_id = session_id
        self._db._session.commit()
        return session_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """
        get_user_from_session_id - gets user for requested session
        Args:
            - session_id: str, user session ID
        Return:
            - User instance corresponding to session ID
        """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """
        destroy_session - destroys a user session
        Args:
            - user_id: int, id corresponding to user
        Return:
            - None
        """
        try:
            user = self._db.find_user_by(id=user_id)
            user.session_id = None
            self._db._session.commit()
        except NoResultFound:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """
        get_reset_password_token - generate a reset password token
        Args:
            - email: str, user email
        Return:
            - reset_token as string
        """
        try:
            user = self._db.find_user_by(email=email)
            new_token = _generate_uuid()
            user.reset_token = new_token
            self._db._session.commit()
            return new_token
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """
        update_password - updates password using generated reset_token
        Args:
            - reset_token: str, generated uuid to verify user
            - password: str, user new password to update
        Return:
            - None
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            password = _hash_password(password)
            user.hashed_password = password
            user.reset_token = None
            self._db._session.commit()
            return None
        except Exception as e:
            raise ValueError
