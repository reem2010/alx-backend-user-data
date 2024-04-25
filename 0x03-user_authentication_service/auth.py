#!/usr/bin/env python3
"""hash module
"""
import bcrypt
from db import DB
from user import Base, User
from sqlalchemy.orm.exc import NoResultFound
import uuid


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

    def valid_login(self, email: str, password: str) -> bool:
        """valid log"""
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode(), user.hashed_password)
        except Exception as e:
            return False

    def create_session(self, email: str) -> str:
        """create session"""
        try:
            User = self._db.find_user_by(email=email)
            session = _generate_uuid()
            setattr(User, 'session_id', session)
            return session
        except Exception as e:
            return None

    def get_user_from_session_id(self, session_id) -> User:
        """get the user"""
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except Exception as e:
            return None

    def destroy_sessions(self, user_id: int) -> User:
        """get the user"""
        try:
            self._db.update_user(user_id, session_id=None)
            return None
        except Exception as e:
            return None


def _generate_uuid() -> str:
    """generate uuid"""
    return str(uuid.uuid4())
