#!/usr/bin/env python3
"""
SessionAuth module for the API
"""
from .auth import Auth
import uuid


class SessionAuth(Auth):
    """ SessionAuth class
    """
    user_id_by_session_id = {}

    def __init__(self):
        pass

    def create_session(self, user_id: str = None) -> str:
        """ Creates session and returns session_id
        """
        if user_id is None:
            return None
        if type(user_id) is not str:
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Returns user_id for a given session_id
        """
        if session_id is None:
            return None
        if type(session_id) is not str:
            return None
        user_id = self.user_id_by_session_id.get(session_id)
        return user_id
