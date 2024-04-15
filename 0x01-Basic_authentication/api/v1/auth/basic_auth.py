#!/usr/bin/env python3
"""
module for basic auth
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """basic auth class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """base 64 method"""
        if(not(authorization_header)):
            return None
        if(type(authorization_header) != str):
            return None
        if(not("Basic " in authorization_header)):
            return None
        return authorization_header[6:]
