#!/usr/bin/python3
from '9-rectangle' import Rectangle
"""Square"""


class Square(Rectangle):
    """Square"""
    def __init__(self, size):
        """Initializes square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
