#!/usr/bin/env python3
"""Auth class module.
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require auth method.
        """
        if path is not None and excluded_paths is not None \
                and len(excluded_paths) > 0:
            for p in excluded_paths:
                if "".join(p.split("/")) == "".join(path.split("/")):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """Authorization header method.
        """
        if request is None or request.headers.get('Authorization') is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user method.
        """
        return None
    
    def session_cookie(self, request=None):
        """Returns a cookie value from a request
        """
        if request is None:
            return None
        return request.cookies.get('_my_session_id')
