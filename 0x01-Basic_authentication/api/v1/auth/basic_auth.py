#!/usr/bin/env python3
"""
module for basic auth
"""
from api.v1.auth.auth import Auth
import base64
from typing import Tuple, TypeVar
from models.user import User


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
        print(res)
        if (len(res) > 2):
            res[1] = ":".join(res[1:])
            print(res[1])
        return tuple(res)

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> User:
        """user object method"""
        if(not(user_email) or type(user_email) != str):
            return None
        if(not(user_pwd) or type(user_pwd) != str):
            return None
        try:
            user = User.search({"email": user_email})
            if(len(user) == 0):
                return None
            user = user[0]
            if (not(user.is_valid_password(user_pwd))):
                return None
            return user
        except Exception as err:
            return None

    def current_user(self, request=None) -> User:
        """CURRENT USER METHOD"""
        header = self.authorization_header(request)
        base_header = self.extract_base64_authorization_header(header)
        decoded = self.decode_base64_authorization_header(base_header)
        credentials = self.extract_user_credentials(decoded)
        return self.user_object_from_credentials(
            credentials[0], credentials[1])
