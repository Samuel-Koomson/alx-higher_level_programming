#!/usr/bin/python3
"""Module defines a class to JSON function"""


def class_to_json(obj):
    """Returns dictionary representation of a simple data structure"""
    return obj.__dict__
