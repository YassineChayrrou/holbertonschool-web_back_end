#!/usr/bin/env python3
""" Auth module """


import bcrypt


def _hash_password(password: str) -> bytes:
    """ hashes a given password """
    password = password.encode()
    salt = bcrypt.gensalt()
    hashed_passwd = bcrypt.hashpw(password, salt)
    return hashed_passwd
