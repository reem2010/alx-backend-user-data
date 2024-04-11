#!/usr/bin/env python3
"""
encrypt password module
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """hash function"""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)
