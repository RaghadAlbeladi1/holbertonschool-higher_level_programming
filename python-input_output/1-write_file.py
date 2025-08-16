#!/usr/bin/python3

"""
Handles writing a string to a specified file
"""


def write_file(filename="", text=""):
    """
    Handles writing data to a file
    """

    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return len(text)
