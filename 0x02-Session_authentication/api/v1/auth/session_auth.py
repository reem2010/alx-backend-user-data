#!/usr/bin/env python3
"""
module for session auth
"""
from api.v1.auth.auth import Auth
import uuid


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
