#!/usr/bin/env python3
"""hash module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """hash function"""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)
