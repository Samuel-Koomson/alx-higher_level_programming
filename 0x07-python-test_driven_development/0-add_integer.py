#!/usr/bin/python3
"""

A module containing a function that adds 2 integers, where it takes in two parameters with the second parameter fixed to a default integer of 98

"""


def add_integer(a, b=98):
    """ This returns the sum of two integers or floats and raise an error if any parameter is not:
    
    Parameters:
        a (first integer or float)
        b (second integer or float set to default 98)
        
    Raises:
        TypeError: If either parameter 'a' or 'b' is not an integer or float
"""
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
