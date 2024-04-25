#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """add user method"""
        session = self._session
        user = User(email=email, hashed_password=hashed_password)
        session.add(user)
        session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """find user"""
        if (not kwargs):
            raise InvalidRequestError
        user = self._session.query(User).filter_by(**kwargs).one()
        if not user:
            raise NoResultFound
        return user

    def update_user(self, user_id: int, **kwargs):
        """update user"""
        user = self.find_user_by(id=user_id)
        keys = User.__table__.columns.keys()
        if (not())
        for key, value in kwargs.items():
            if (not(key in keys)):
                raise ValueError
            setattr(user, key, value)
        self._session.commit()
