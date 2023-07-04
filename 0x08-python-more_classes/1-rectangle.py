#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """Creates a rectangle"""

    @property
    def width(self):
        """Get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        if not isinstance(height, int):
            raise TypeError('width must be an integer')
        if height < 0:
            raise ValueError('width must be >= 0')
        self.__height = height

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle"""
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width
        if not isinstance(height, int):
            raise TypeError('width must be an integer')
        if height < 0:
            raise ValueError('width must be >= 0')
        self.__height = height
