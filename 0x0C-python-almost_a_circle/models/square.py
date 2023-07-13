#!/usr/bin/python3
"""Square"""


Rectangle = __import__('rectangle').Rectangle
class Square(Rectangle):
    """square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class init method"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.__width

    @size.setter
    def size(self, val):
        if type(val) != int:
            raise TypeError('size must be an integer')
        if val <= 0:
            raise ValueError('size must be > 0')
        self.__width = val
        self.__height = val

    def __str__(self):
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'
