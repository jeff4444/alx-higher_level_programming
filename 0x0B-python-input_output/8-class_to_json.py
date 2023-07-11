#!/usr/bin/python3
"""Class to JSON object"""


def class_to_json(obj):
    """Converts a class to a json object"""
    my_dict = obj.__dict__
    return my_dict
