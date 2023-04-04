#!/usr/bin/python3
"""

A module containing a function that prints a name made up of strings.

"""


def say_my_name(first_name, last_name):
    """ The function takes two arguements and prints first name and last name
    
    Parameters:
        first_name (first name being printed which is a string)
        last_name (second name being printed which is a string)
        
    Raises:
        TypeError: first_name must be a string or last_name must be a string
         
"""     
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
