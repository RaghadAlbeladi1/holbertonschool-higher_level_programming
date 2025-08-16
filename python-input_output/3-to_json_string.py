#!/usr/bin/python3
"""Module encodes data to json"""


import json


def to_json_string(my_obj):
    """return encoded data"""
    return json.dumps(my_obj)
