#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.state import State


class City(BaseModel, Base):
    """City class for storing city information"""
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(60), nullable=False)
    places = relationship('Place', cascade='all, delete', backref='cities')
