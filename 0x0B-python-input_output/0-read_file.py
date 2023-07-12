#!/usr/bin/python3
"""read file module"""


def read_file(filename=""):
    """read file function"""
    with open(filename, 'r', encoding='utf-8') as f:
        read = f.read()
        print(read[:-1])

read_file('file.txt')
