#!/usr/bin/env python3
"""hash module
"""
import bcrypt
from db import DB
from user import Base, User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """hash function"""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """register user"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User " + email + " already exists")
        except NoResultFound:
            password = _hash_password(password)
            return self._db.add_user(email=email, hashed_password=password)
