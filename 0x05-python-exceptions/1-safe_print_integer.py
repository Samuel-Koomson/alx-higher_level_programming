#!/usr/bin/python3
def safe_print_integer(value):
    """ Function Prints an integer with "{:d}".format().
    Args:
        value (int): The integer being printed.
    Returns:
        False if  a TypeError or ValueError occurs
        Otherwise return True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
