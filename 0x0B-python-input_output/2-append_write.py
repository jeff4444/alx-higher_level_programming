#!/usr/bin/python3
"""Append to file"""


def append_write(filename="", text=""):
    """append file module"""
    with open(filename, 'a', encoding='utf-8') as f:
        length = f.write(text)
    return length
