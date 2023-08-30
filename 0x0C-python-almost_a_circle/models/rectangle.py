#!/usr/bin/python3
"""Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init method"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets width"""
        return self.__width

    @width.setter
    def width(self, val):
        """Sets width"""
        if type(val) != int:
            raise TypeError('width must be an integer')
        if val <= 0:
            raise ValueError('width must be > 0')
        self.__width = val

    @property
    def height(self):
        """Gets height"""
        return self.__height

    @height.setter
    def height(self, val):
        """Sets height"""
        if type(val) != int:
            raise TypeError('height must be an integer')
        if val <= 0:
            raise ValueError('height must be > 0')
        self.__height = val

    @property
    def x(self):
        """Gets x"""
        return self.__x

    @x.setter
    def x(self, val):
        """sets x"""
        if type(val) != int:
            raise TypeError('x must be an integer')
        if val < 0:
            raise ValueError('x must be >= 0')
        self.__x = val

    @property
    def y(self):
        """gets y"""
        return self.__y

    @y.setter
    def y(self, val):
        """Sets y"""
        if type(val) != int:
            raise TypeError('y must be an integer')
        if val < 0:
            raise ValueError('y must be >= 0')
        self.__y = val

    def area(self):
        """Returns area of Rectangle"""
        return self.__width * self.__height

    def display(self):
        """Displays rectangle"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            string = ' ' * self.__x
            string += '#' * self.__width
            print(string)

    def __str__(self):
        """Returns str(Rectangle) in desired form"""
        string = f'[Rectangle] ({self.id}) {self.x}/{self.y} - '
        string += f'{self.width}/{self.height}'
        return string

    def update(self, *args, **kwargs):
        """Updates Rectangle"""
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            i = 0
            for arg in args:
                setattr(self, attrs[i], arg)
                i += 1
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """Converts instance to dict object"""
        dic = {}
        dic['x'] = self.__x
        dic['y'] = self.__y
        dic['width'] = self.__width
        dic['height'] = self.__height
        dic['id'] = self.id
        return dic
