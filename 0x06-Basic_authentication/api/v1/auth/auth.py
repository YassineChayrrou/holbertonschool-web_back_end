#!/usr/bin/env python3
""" API authentication management model
"""


from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class
    """

    def __init__(self):
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Public method require_auth
        """
        return False

    def authorization_header(self, request=None) -> TypeVar('User'):
        """ Public method authorization_header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Public method current_user
        """
        return None
