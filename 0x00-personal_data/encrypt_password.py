#!/usr/bin/env python3
"""
Password Encryption and Validation Module
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
        Generates a hashed and salted password.
        Args:
                password(str):The plain text
                password to be hashed.
        Returns:
                bytes: A byte string representing the salted, hashed password.
        """
    encoded_password = password.encode()
    hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
        checks whether the provided password matches the hashed password.
        Args:
                hashed_password(bytes): A byte string representing
                the salted, hashed password.
                password(str): A string containing the plain text
                password to be validated.
        Returns:
                bool: True if the provided password matches the hashed
                password else return False
        """
    is_valid = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        is_valid = True
    return is_valid
