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
        return False

    def authorization_header(self, request=None) -> str:
        """auth method"""
        return None

    def current_user(self, request=None) -> User:
        """current user"""
        return None
