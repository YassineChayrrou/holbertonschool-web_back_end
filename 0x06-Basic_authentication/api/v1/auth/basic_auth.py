#!/usr/bin/env python3
"""BasicAuth model"""


from .auth import Auth
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
        except binascii.Error:
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
            return tuple(decoded_base64_authorization_header.split(":"))
