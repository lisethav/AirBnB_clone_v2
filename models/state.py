#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
            'City', backref='state', cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """Returns cities obj """
            new_list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    new_list.append(city)
            return (new_list)
