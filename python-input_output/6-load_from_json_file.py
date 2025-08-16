#!/usr/bin/python3
"""Module creates an object"""


import json


def load_from_json_file(filename):
    """Module creates an object"""
    with open(filename, 'r', encoding='utf-8')as f:
        return json.load(f)
