#!/usr/bin/python3
"""Rectangle"""


from '7-base_geometry' import BaseGeometry
class Rectangle(BaseGeometry):
    """Rectangle"""
    def __init__(self, width, height):
        """Initialises Rectangle"""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
