#!/usr/bin/env python3
"""
module for basic auth
"""
from api.v1.auth.auth import Auth
import base64
from typing import Tuple


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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """base 64 decode method"""
        if(not(base64_authorization_header)):
            return None
        if(type(base64_authorization_header) != str):
            return None
        try:
            decode_bytes = base64.b64decode(base64_authorization_header)
            return decode_bytes.decode('utf-8')
        except Exception as err:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> Tuple[str, str]:
        """extract user method"""
        if(not(decoded_base64_authorization_header)):
            return (None, None)
        if(type(decoded_base64_authorization_header) != str):
            return (None, None)
        if(not(":" in decoded_base64_authorization_header)):
            return (None, None)
        res = decoded_base64_authorization_header.split(":")
        return tuple(res)
