#!/usr/bin/env python3
""" SessionDBAuth module
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user import User
from models.user_session import UserSession
from typing import TypeVar
import uuid
from datetime import datetime


class SessionDBAuth(SessionExpAuth):
    """ SessionDBAuth class
    """

    def create_session(self, user_id: str = None) -> str:
        """ Create a session
        """
        if user_id is None:
            return None
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        user_session = UserSession(user_id=user_id, session_id=session_id)
        user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Get a user ID from a session ID
        """
        if session_id is None:
            return None
        user_session = UserSession.search({'session_id': session_id})
        if user_session is None or len(user_session) == 0:
            return None
        user_session = user_session[0]
        if user_session is None:
            return None
        if user_session.expired:
            return None
        return user_session.user_id

    def destroy_session(self, request=None) -> bool:
        """ Destroy a session
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False
        user_sessions = UserSession.search({'session_id': session_id})
        if user_sessions is None or len(user_sessions) == 0:
            return False
        for user_session in user_sessions:
            user_session.remove()
        return True
