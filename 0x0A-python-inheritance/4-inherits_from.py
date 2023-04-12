#!/usr/bin/python3
"""function defines inherit from function"""


def inherits_from(obj, a_class):
    """inherits the details of a class"""
    if issubclass(type(obj), (a_class)) and type(obj) is not a_class:
        return True
    return False
