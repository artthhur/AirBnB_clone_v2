#!/usr/bin/python3
""" Amenity Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models import storage_type


class Amenity(BaseModel, Base):
    """Represents Amenity Class"""
    __tablename__ = 'amenities'

    if storage_type != 'db':
        name = ""
    else:
        name = Column(String(128), nullable=False)
