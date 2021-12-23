#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
import models
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import backref, relationship
from models.city import City
from models import storage

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullbase=False)
    cities = relationship('City', backref=backref(
                        "state", cascade="all, delete"))
    
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Returns all cities in state"""
            new_list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    new_list.append(city)
            return new_list
