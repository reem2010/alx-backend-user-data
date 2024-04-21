#!/usr/bin/env python3
"""
module for session deb auth
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """session db class"""

    def create_session(self, user_id=None):
        """create session"""
        session_id = super().create_session(user_id)
        if(not(session_id)):
            return None
        user_session = UserSession({
            "user_id": user_id,
            "session_id": session_id})
        user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """user id"""
        try:
            user = UserSession.search({"session_id": session_id})
            return user.get("user_id")
        except Exception as err:
            return None

    def destroy_session(self, request=None):
        """destroy session"""
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if (not(session_id)):
            return False
