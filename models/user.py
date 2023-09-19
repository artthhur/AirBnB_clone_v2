#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from models.place import Place
from models.review import Review
from sqlalchemy import Column, String
from models import storage_type
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes
    class Attributes:
        __tablename__: mapping table
        email: sqlalchemy String column: user's email
        password: sqlalchemy String column: user's password
        first_name: sqlalchemy String column: user's firstname
        last_name: sqlalchemy String column: user's lastname
    """
    __tablename__ = 'users'

    if storage_type != 'db':
        email = ''
        password = ''
        first_name = ''
        last_name = ''
    else:
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('Place', backref='user',
                              cascade='all, delete')
        reviews = relationship('Review', backref='user',
                               cascade='all, delete')
