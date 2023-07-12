#!/usr/bin/python3
"""Add attributes to a class"""


def add_attribute(obj, key, val):
    """add attr func"""
    if getattr(obj, key, None) is not None:
        raise TypeError("can't add new attribute")
    elif not isinstance(key, str):
        raise TypeError("can't add new attribute")
    elif isinstance(obj, str):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, key, val)
