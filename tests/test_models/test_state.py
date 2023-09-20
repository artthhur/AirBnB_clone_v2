#!/usr/bin/python3
"""This module contains test cases for State model """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
from models import storage_type


class test_state(test_basemodel):
    """ State test Class"""

    def __init__(self, *args, **kwargs):
        """ Initialise state test class"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ test case for name attribute """
        new = self.value()
        if storage_type != 'db':
            self.assertEqual(type(new.name), str)
        else:
            self.assertEqual(type(new.name), type(None))
