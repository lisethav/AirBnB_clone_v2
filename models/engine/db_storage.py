#!/usr/bin/python3
"""
This is the db_storage class for Airbnb
"""
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import (sessionmaker, scoped_session)
from os import getenv
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State



class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """ initializes engine """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                getenv('HBNB_MYSQL_USER'),
                                getenv('HBNB_MYSQL_PWD'),
                                getenv('HBNB_MYSQL_HOST'),
                                getenv('HBNB_MYSQL_DB')))
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query on the current database session """
        list_obj = []
        if cls:
            list_obj = self.__session.query(cls).all()
        else:
            for cls in (State, City, Place, Amenity, Review, User):
                list_obj.extend(self.__session.query(cls).all())
        return {"{}.{}".format(type(cls)._name_, cls.id): cls for cls in list_obj}

    def new(self, obj):
        """ add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ create all tables in the database """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)()

    def close(self):
        """ close a session """
        self.__session.close()
        