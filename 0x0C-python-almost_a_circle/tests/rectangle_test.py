#!/usr/bin/python3
"""rectangle class test suite"""


import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """TestRectangle class"""

    def test_init(self):
        """test the init method of Rectangle"""
        r1 = Rectangle(1, 2, 3, 4, 1)
        out = [r1.width, r1.height, r1.x, r1.y, r1.id]
        inp = [1, 2, 3, 4, 1]
        self.assertEqual(out, inp)
        r2 = Rectangle(1, 2, 0, 0, 2)
        out = [r2.width, r2.height, r2.x, r2.y, r2.id]
        inp = [1, 2, 0, 0, 2]
        self.assertEqual(out, inp)

    def test_setters(self):
        """test the setters in Rectangle"""
        self.assertRaises(TypeError, Rectangle, 1, '2')
        self.assertRaises(TypeError, Rectangle, [1], 2)
        self.assertRaises(ValueError, Rectangle, -1, 1)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(ValueError, Rectangle, 1, 1, -1)
        self.assertRaises(TypeError, Rectangle, 1, 1, 2, {})

    def test_area(self):
        """test area methodd in rectange"""
        r = Rectangle(2, 3, 3, 1, 2)
        self.assertEqual(6, r.area())

    def test_str(self):
        """test the str function in rectangle"""
        r = Rectangle(2, 3, 4, 5, 6)
        string = "[Rectangle] (6) 4/5 - 2/3"
        self.assertEqual(string, str(r))

    def test_update(self):
        """Test the update method in rectangle"""
        r = Rectangle(2, 3, 4, 5, 6)
        string = "[Rectangle] (6) 4/5 - 2/3"
        self.assertEqual(string, str(r))
        r.update(4)
        string = "[Rectangle] (4) 4/5 - 2/3"
        self.assertEqual(string, str(r))
        r.update(4, 11, 12)
        string = "[Rectangle] (4) 4/5 - 11/12"
        self.assertEqual(string, str(r))
        r.update(10, 11, 12, 13, 14)
        string = "[Rectangle] (10) 13/14 - 11/12"
        self.assertEqual(string, str(r))
        r.update(height=1, width=2, x=3, id=89, y=4)
        string = "[Rectangle] (89) 3/4 - 2/1"
        self.assertEqual(string, str(r))

    def test_to_dict(self):
        """test the to dictionary method in rectangle"""
        r = Rectangle(2, 3, 4, 5, 6)
        dicti = r.to_dictionary()
        self.assertEqual(2, dicti['width'])
        self.assertEqual(3, dicti['height'])
        self.assertEqual(4, dicti['x'])
        self.assertEqual(5, dicti['y'])
        self.assertEqual(6, dicti['id'])

    def test_to_json_string(self):
        import json
        r = Rectangle(10, 11, 12, 13, 14)
        dic = r.to_dictionary()
        json_dict = Base.to_json_string([dic])
        string = json.dumps([dic])
        self.assertEqual(string, json_dict)
        json_dict = Base.to_json_string(None)
        string = '[]'
        self.assertEqual(string, json_dict)
        json_dict = Base.to_json_string([])
        self.assertEqual(string, json_dict)

    def test_save_to_file(self):
        """test the save_to_file method in rectangle"""
        import json
        r = Rectangle(10, 7, 2, 8, 2)
        dic = r.to_dictionary()
        r1 = Rectangle(1, 2, 3, 4, 5)
        dic1 = r1.to_dictionary()
        string = json.dumps([dic, dic1])
        Rectangle.save_to_file([r, r1])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(string, f.read())
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual('[]', f.read())

    def test_from_json_string(self):
        """test the from_json_string method in rectangle"""
        import json
        inpt = [{'id': 89, 'width': 10, 'height': 4},
                {'id': 7, 'width': 1, 'height': 7}]
        json_inpt = Rectangle.to_json_string(inpt)
        outpt = Rectangle.from_json_string(json_inpt)
        self.assertEqual(inpt, outpt)
        outpt = Rectangle.from_json_string(None)
        self.assertEqual([], outpt)
        outpt = Rectangle.from_json_string('[]')
        self.assertEqual([], outpt)

    def test_create(self):
        """test the create method in rectangle"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        dicti = r1.to_dictionary()
        r2 = Rectangle.create(**dicti)
        self.assertEqual(str(r1), str(r1))
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_load_from_file(self):
        """Test the load from file method in rectangle"""
        r1 = Rectangle(1, 2, 3, 4, 4)
        r2 = Rectangle(5, 6, 7, 8, 9)
        rect_list = [r1, r2]
        Rectangle.save_to_file(rect_list)
        rect_list_out = Rectangle.load_from_file()
        for i in range(len(rect_list)):
            self.assertEqual(str(rect_list[i]), str(rect_list_out[i]))
