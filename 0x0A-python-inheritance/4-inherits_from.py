#!/usr/bin/python3
"""inherits_from"""


def inherits_from(obj, a_class):
    """ returns True if obj is an instance of a_class"""
    if issubclass(type(obj), a_class):
        return not (type(obj) is a_class)
    return False
