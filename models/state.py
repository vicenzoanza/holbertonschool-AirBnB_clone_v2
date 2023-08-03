#!/usr/bin/python3
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from os import getenv


class State(BaseModel, Base):
    """State class for storing state information"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", cascade="all, delete", backref="state")
    else:
        @property
        def cities(self):
            from models import storage
            from models.city import City
            cities_list = []
            for key,value in storage.all(City):
                if value["state_id"] == self.id:
                    cities_list.append(value)
            return cities_list