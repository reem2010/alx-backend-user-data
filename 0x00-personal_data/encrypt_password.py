#!/usr/bin/env python3
"""
encrypt password module
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """hash function"""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)


def is_valid(hashed_password: bytes, password: str):
    """valid passfunction"""
    return bcrypt.checkpw(password.encode(), hashed_password)
