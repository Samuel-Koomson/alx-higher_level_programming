#!/usr/bin/python3
"""function checks if object is an instance of a class
or an inherited class
"""
def is_kind_of_class(obj, a_class):
    """returns True if is instance otherwise False"""
    return (isinstance(obj, a_class))
