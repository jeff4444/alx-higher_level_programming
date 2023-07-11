#!/usr/bin/python3
"""Write to files"""


def write_file(filename="", text=""):
    """ write file module"""
    with open(filename, 'w', encoding='utf-8') as f:
        length = f.write(text)
    return length
