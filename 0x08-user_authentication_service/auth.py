#!/usr/bin/env python3
""" Auth module
    manages authentication related operations
    main imports:
        - bcrypt
    module name 'auth'
"""


import bcrypt


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
