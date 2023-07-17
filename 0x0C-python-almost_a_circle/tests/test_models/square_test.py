#!/usr/bin/python3
"""Square class tests suite"""


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """TestSquare class"""

    def test_init(self):
        """tests the init method of Square"""
        s = Square(5)
        self.assertEqual(25, s.area())
        s1 = Square(3, 1, 4, 2)
        self.assertEqual(9, s1.area())
        self.assertEqual("[Square] (2) 1/4 - 3", str(s1))
        self.assertEqual(5, s.size)
        self.assertRaises(TypeError, Square, '2')
        self.assertRaises(TypeError, Square, [])
        self.assertRaises(TypeError, Square, {})
        self.assertRaises(ValueError, Square, 0)
        self.assertRaises(ValueError, Square, -1)

    def test_update(self):
        """test the update method in Square class"""
        s = Square(1, 0, 0, 8)
        self.assertEqual("[Square] (8) 0/0 - 1", str(s))
        s.update(3, 2, 1, 2)
        self.assertEqual("[Square] (3) 1/2 - 2", str(s))
        s.update(2, 1)
        self.assertEqual("[Square] (2) 1/2 - 1", str(s))
        s.update(size=2, y=2, x=6, id=99)
        self.assertEqual("[Square] (99) 6/2 - 2", str(s))

    def test_to_dict(self):
        """Test the to dictionary method in Square"""
        s = Square(1, 2, 3, 4)
        dic = s.to_dictionary()
        self.assertEqual(1, dic['size'])
        self.assertEqual(2, dic['x'])
        self.assertEqual(3, dic['y'])
        self.assertEqual(4, dic['id'])

    def test_load_file(self):
        """Tests the load fro file method in Square"""
        s1 = Square(5, 0, 0, 3)
        s2 = Square(2, 3, 4, 3)
        list_sq = [s1, s2]
        Square.save_to_file(list_sq)
        list_sq_out = Square.load_from_file()
        for i in range(len(list_sq)):
            self.assertEqual(str(list_sq[i]), str(list_sq_out[i]))
