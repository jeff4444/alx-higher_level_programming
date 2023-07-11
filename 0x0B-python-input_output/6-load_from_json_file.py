#!/usr/bin/python3
"""Load from JSON"""


def load_from_json_file(filename):
    """Load from json func"""
    import json
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
