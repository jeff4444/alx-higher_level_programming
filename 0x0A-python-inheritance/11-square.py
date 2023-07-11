#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""Square"""


class Square(Rectangle):
    """Square"""
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return f'[Square] {self.__size}/{self.__size}'
