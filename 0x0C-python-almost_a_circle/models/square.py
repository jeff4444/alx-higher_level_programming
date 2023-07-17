#!/usr/bin/python3
"""Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class init method"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """gets size"""
        return self.width

    @size.setter
    def size(self, val):
        """sets size"""
        if type(val) != int:
            raise TypeError('size must be an integer')
        if val <= 0:
            raise ValueError('size must be > 0')
        self.width = val
        self.height = val

    def __str__(self):
        """Recturns str(Square) in desired form"""
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.size}'

    def update(self, *args, **kwargs):
        """Updates Square instance"""
        if args:
            attrs = ['id', 'size', 'x', 'y']
            i = 0
            for arg in args:
                setattr(self, attrs[i], arg)
                i += 1
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """Returns dict object of instance"""
        dic = {}
        dic['x'] = self.x
        dic['y'] = self.y
        dic['size'] = self.height
        dic['id'] = self.id
        return dic
