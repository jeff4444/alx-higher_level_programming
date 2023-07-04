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
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle"""
        self.__width = width
        self.__height = height

    def area(self):
        """Return Area of Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return printed rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ''
        string = ''
        for _ in range(self.__height):
            for _ in range(self.__width):
                string += '#'
            string += '\n'
        return string
