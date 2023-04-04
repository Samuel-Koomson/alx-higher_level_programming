#!/usr/bin/python3
"""

A module containing a function that prints a square using the # symbol.

"""


def print_square(size):
    """ The function takes two only one arguements and prints a square using the # symbol
    
    Parameters:
        size: (length of square to be printed)
        
    Raises:
        TypeError: If size is not an integer
        TypeError: If size is a float and less than zero
        ValueError: If size is less than zero
         
"""     
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for x in range(0, size):
        for y in range(size):
            print("#", end="")
        print("")
