#!/usr/bin/env python3
"""
module for auth
"""
import os
from flask import request
from typing import List, TypeVar
User = TypeVar('User')


class Auth():
    """auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require auth method"""
        if (not (path) or not(excluded_paths) or len(excluded_paths) == 0):
            return True
        if (path[-1] != '/'):
            path = path + "/"
        for var in excluded_paths:
            if (var[-1] == "*") and var[:-1] in path:
                return False
            if (path == var):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """auth method"""
        if (not(request) or not('Authorization' in request.headers)):
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> User:
        """current user"""
        return None

    def session_cookie(self, request=None):
        """cookie value"""
        if(not(request)):
            return None
        key = os.getenv('SESSION_NAME')
        return request.cookies.get(key)
