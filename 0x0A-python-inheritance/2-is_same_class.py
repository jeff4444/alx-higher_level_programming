#!/usr/bin/python3
"""is_same_class"""


def is_same_class(obj, a_class):
    """ returns True if obj is an instance of a_class"""
    return type(obj) == type(a_class)
