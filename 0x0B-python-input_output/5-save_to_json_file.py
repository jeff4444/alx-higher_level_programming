#!/usr/bin/python3
"""Save JSON to a file"""


def save_to_json_file(my_obj, filename):
    """save to json file func"""
    import json
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
