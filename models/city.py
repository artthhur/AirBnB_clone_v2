#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import Column, String, ForeignKey
from models import storage_type
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """Represents the city class
    Class Attribute:
        __tablename__: the mapping table
        name: sqlalchemy String Column : the city name
        state_id: sqlalchemy String Column : the state identifier (FK)
    """
    __tablename__ = 'cities'

    if storage_type != 'db':
        name = ''
        state_id = ''
    else:
        name = Column(String(128), nullable=False)
        state_id = Column(String(60),
                          ForeignKey("states.id"),
                          nullable=False)
        places = relationship('Place', backref='cities',
                              cascade='all, delete')
