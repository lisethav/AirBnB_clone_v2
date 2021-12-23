#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from models.base_model import Base


class City(BaseModel, Base):

    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
