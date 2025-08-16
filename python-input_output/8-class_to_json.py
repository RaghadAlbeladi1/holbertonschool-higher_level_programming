#!/usr/bin/python3
"""Retruns dictionary description"""


def class_to_json(obj):
    """Returns dictionary"""
    return obj.__dict__.copy()
