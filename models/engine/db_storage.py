#!/usr/bin/python3
"""Contains the DBStorage Class"""
from os import getenv
import MySQLdb
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.base_model import Base


class DBStorage:
    """ Class DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')),
                pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
        Return the table or the tables.
        """
        from console import HBNBCommand

        info = {}
        if cls in HBNBCommand.classes.values():
            result = self.__session.query(cls).all()
            for x in result:
                info[f"{cls}.{x.id}"] = x.to_dict()
        else:
            for table in HBNBCommand.classes.values():
                if table.__name__ != 'BaseModel':
                    result = self.__session.query(table).all()
                    for x in result:
                        string = f"{table.__class__.__name__}.{x.id}"
                        info[string] = x.to_dict()
        return info

    def new(self, obj):
        """ Add the obj at the database"""
        self.__session.add(obj)

    def save(self):
        """ Save changes in the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete obj of the database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Relaod"""
        Base.metadata.create_all(self.__engine)
        current_session = sessionmaker(self.__engine, expire_on_commit=False)
        self.__session = scoped_session(current_session)
