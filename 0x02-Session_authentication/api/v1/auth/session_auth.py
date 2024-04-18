#!/usr/bin/env python3
"""
module for session auth
"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """SESSION CLASS"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates a Session ID"""
        if(not(user_id)):
            return None
        if(type(user_id) != str):
            return None
        session_id = str(uuid.uuid4())
        SessionAuth.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """user id of session id"""
        if(not(session_id)):
            return None
        if(type(session_id) != str):
            return None
        return SessionAuth.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """RETURN CURRENT USER"""
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        if (not(user_id)):
            return None
        return User.get(user_id)
