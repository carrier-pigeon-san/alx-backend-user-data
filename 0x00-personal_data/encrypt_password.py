#!/usr/bin/env python3
""" A module that implements various password encryption functionalities """
import bcrypt


def hash_password(password: str) -> bytes:
    """ Returns a salted, hashed password, which is encoded in
    bytes """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Checks if the password matches the hashed password """
    return bcrypt.checkpw(password.encode(), hashed_password)
