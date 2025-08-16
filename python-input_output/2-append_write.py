#!/usr/bin/python3
"""Append text to a file"""


def append_write(filename="", text=""):
    """Appends text to a file"""
    with open(filename, 'a', encoding='utf-8') as f:
        count = f.write(text)
    return count
