#!/usr/bin/env python3
"""SessionDBAuth module
"""


from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """ SessionDBAuth class
    """
    def create_session(self, user_id=None):
        """ Overloads SessionExpAuth create_session
        """
        pass
