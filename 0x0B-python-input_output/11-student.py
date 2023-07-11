#!/usr/bin/python3
"""Student class"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return sthe json object of self"""
        if attrs is None:
            return self.__dict__
        return dict(list(filter((lambda x: x[0] in attrs),
                    self.__dict__.items())))

    def reload_from_json(self, json):
        """Reload object from json"""
        for key, val in json.items():
            setattr(self, key, val)
