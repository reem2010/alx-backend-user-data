#!/usr/bin/env python3
"""
module for auth
"""
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
        if (path in excluded_paths):
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
