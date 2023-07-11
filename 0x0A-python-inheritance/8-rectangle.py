#!/usr/bin/python3
from '7-base_geometry' import BaseGeometry
"""Rectangle"""


class Rectangle(BaseGeometry):
    """Rectangle"""
    def __init__(self, width, height):
        """Initialises Rectangle"""
        BaseGeometry.integer_validator(self, 'width', width)
        BaseGeometry.integer_validator(self, 'height', height)
        self.__width = width
        self.__height = height
