#!/usr/bin/python3
"""
This module defines a class to manage database storage for hbnb clone
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os


class DBStorage:
    """
    Database storage engine
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Creates a linked to the MySQL database
        """
        username = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        hostname = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(username, password, hostname,
                                             database), pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Returns a dictionary of models currently in storage
        """
        if cls is None:
            classes = [User, State, City, Amenity, Place, Review]
        else:
            classes = [cls]

        obj_dict = {}
        for cls in classes:
            query = self.__session.query(cls).all()
            for obj in query:
                class_name = obj.__class__.__name__
                obj_id = obj.id
                key = "{}.{}".format(class_name, obj_id)
                obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """
        Adds new object to storage dictionary
        """
        self.__session.add(obj)

    def save(self):
        """
        Saves storage dictionary to file
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes obj from __objects if its inside
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Refreshes __session with current database
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        Closes a session
        """
        self.__session.remove()
