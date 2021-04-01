#!/usr/bin/env python3
"""BasicAuth model"""


from .auth import Auth


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
