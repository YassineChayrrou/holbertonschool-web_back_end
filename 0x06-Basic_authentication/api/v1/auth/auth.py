#!/usr/bin/env python3
""" API authentication management model
"""


from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class
    """

    def __init__(self):
        """ Auth class constructor
        """
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Public method require_auth
        """
        regex_excluded_paths = []

        if path is None:
            return True

        if not excluded_paths:
            return True

        for excluded_path in excluded_paths:
            if excluded_path[-1] == "*":
                regex_excluded_paths.append(excluded_path[:-1])
        for i in regex_excluded_paths:
            if i in path:
                return False

        if path[-1] != '/':
            path = path + '/'
        if path not in excluded_paths:
            return True
        return False

    def authorization_header(self, request=None) -> TypeVar('User'):
        """ Public method authorization_header
        """
        if request is None:
            return None
        if 'Authorization' in request.headers:
            return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """ Public method current_user
        """
        return None
