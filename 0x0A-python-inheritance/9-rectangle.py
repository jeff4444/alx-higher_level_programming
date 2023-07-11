#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Rectangle"""


class Rectangle(BaseGeometry):
    """Rectangle"""
    def __init__(self, width, height):
        """Initialises Rectangle"""
        BaseGeometry.integer_validator(self, 'width', width)
        BaseGeometry.integer_validator(self, 'height', height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f'[Rectangle] {self.__width}/{self.__height}'
