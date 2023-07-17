#!/usr/bin/python3
"""Base class test suite"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """TestBase class"""

    def test_id(self):
        """tests the id assignment of the base class"""
        b = Base()
        self.assertEqual(b.id, 1)
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b2 = Base(6)
        self.assertEqual(b2.id, 6)
        b3 = Base()
        self.assertEqual(b3.id, 3)
