#!/usr/bin/python3
"""BaseGeometry"""


class BaseGeometry:
    """BaseGeometry class"""

    def __init__(self):
        """Init function"""
        pass

    def area(self):
        """Area function"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """int validator"""
        if type(value) != int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
