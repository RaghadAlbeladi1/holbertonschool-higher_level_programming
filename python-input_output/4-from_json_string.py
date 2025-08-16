#!/usr/bin/python3
"""Moduke decodes str"""


import json


def from_json_string(my_str):
    """Decodes str"""
    return json.loads(my_str)
