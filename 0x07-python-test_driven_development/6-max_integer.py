#!/usr/bin/python3
"""
A module containing a function that finds the maximum integer in a list
"""


def max_integer(list =[]):
    """ The function finds and returns the maximum integer in a list of integers, and returns None if the list is empty
    """     
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
