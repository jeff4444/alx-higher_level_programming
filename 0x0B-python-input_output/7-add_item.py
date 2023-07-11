#!/usr/bin/python3
"""Load, add, save"""


import json
import sys


def main():
    """main function, will load, add and save object to json"""
    filename = 'add_item.json'
    with open(filename, 'r', encoding='utf-8') as f:
        try:
            cur_obj = json.load(f)
        except json.decoder.JSONDecodeError:
            cur_obj = []
        for i in range(1, len(sys.argv)):
            cur_obj.append(sys.argv[i])
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(cur_obj, f)


main()
