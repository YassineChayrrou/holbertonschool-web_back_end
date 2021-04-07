#!/usr/bin/env python3
""" SessionExpAuth module
"""


from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime
from datetime import timedelta


class SessionExpAuth(SessionAuth):
    """ SessionAuth class
    """
    def __init__(self):
        """ Class constructor
        """
        try:
            self.session_duration = int(getenv('SESSION_DURATION'))
        except Exception as e:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """ overloads create_session at SessionAuth
        """
        session_id = super().create_session(user_id)
        # print(session_id)
        if not session_id:
            return None
        created_at = datetime.now()
        self.user_id_by_session_id[session_id] = {'user_id': user_id,
                                                  'created_at': created_at
                                                  }
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ overloads user_id_for_session_id in SessionAuth
        """
        if session_id is None:
            return None
        session_dictionary = self.user_id_by_session_id.get(session_id)
        if session_dictionary is None:
            return None
        if self.session_duration <= 0:
            return session_dictionary.get('user_id')
        created_at = session_dictionary.get('created_at')
        if created_at is None:
            return None
        expiration = created_at + timedelta(seconds=self.session_duration)
        if expiration < datetime.now():
            return None
        return session_dictionary.get('user_id')
