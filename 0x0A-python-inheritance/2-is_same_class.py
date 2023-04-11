#!/usr/bin/python3
"""Function checks if object is an instance of a class"""


def is_same_class(obj, a_class):
    """This returns true if object is an instance of 
    class, or return false
    """
    return (type(obj) == a_class)
