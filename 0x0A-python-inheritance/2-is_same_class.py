#!/usr/bin/python3
"""is_same_class"""


def is_same_class(obj, a_class):
    """ returns True if obj is an instance of a_class"""
    return str(type(obj)) == str(type(a_class))
