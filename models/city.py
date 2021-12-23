#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy.sql.expression import false
from sqlalchemy.sql.schema import ForeignKey
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullbase=false)
