#!/usr/bin/env python3
""" DB module
    manages CRUD operations on local sqlite database using sqlalchemy
    main imports:
        - sqlalchemy pip3 installed
        - user: local module in file 'user.py'
    module name 'db'
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import Base, User
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


class DB:
    """
    DB class:
        - Role: manages CRUD operations in DB
        - class methods:
            + _session
            + add_user
            + find_user_by
            + update_user
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
        """ Memoized session object
            initiate a session if not exists
            Returns:
                - Session
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        add_user - adds User to database and commit changes
        Args:
            - email: user email of string type
            - hashed_password of string type
        Return:
            - User instance
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """
        find_user_by - Finds a user using keyword as argument
        Args:
            - kwargs: dictionary -> dict[(user_attribute)] = (attribute_value)
                + Format: user_attribute=attribute_value
        Return:
            - user instance if exists
            - raises NoResultFound or InvalidRequestError
        """
        try:
            user = self.__session.query(User).filter_by(**kwargs).first()
        except InvalidRequestError:
            raise InvalidRequestError
        if user is None:
            raise NoResultFound
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        update_user - updates user in DataBase and commit changes to session
        Args:
            - user_id: int, checks for user.id in DB
            - kwargs: dictionary -> dict[(user_attribute)] = (attribute_value)
                + Format: user_attrib=attribute_value
        Return:
            - None
        """
        my_user = self.find_user_by(id=user_id)

        for key in kwargs:
            if hasattr(my_user, key) is False:
                raise ValueError
            setattr(my_user, key, kwargs[key])
        self._session.commit()
        return None
