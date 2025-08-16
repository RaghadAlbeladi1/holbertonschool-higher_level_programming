#!/usr/bin/python3
""" Module to read and print a text file """


def read_file(filename=""):
    """ read_file - reads a file and prints it to stdout """
    with open(filename, encoding='utf-8') as a_file:
        print(a_file.read(), end="")
