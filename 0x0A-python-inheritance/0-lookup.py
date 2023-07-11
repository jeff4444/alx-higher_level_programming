#!/usr/bin/python3
""" loopup method """


def lookup(obj):
    """ return list of available attributes in obj """
    return [item for item in dir(obj)]
