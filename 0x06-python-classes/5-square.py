#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initialize a new Square

        Args: size (int): The size of a new square.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Calculares the area of the square"""
        return self.__size * 2

    @property
    def size(self):
        """ Returns the size. """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        """Prints the square"""
        if self.__size == 0:
            print()
        for _ in range(self.__size):
            for _ in range(self.__size):
                print('#', end='')
            print()
