#!/usr/bin/python3
"""Student class"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return sthe json object of self"""
        return self.__dict__
