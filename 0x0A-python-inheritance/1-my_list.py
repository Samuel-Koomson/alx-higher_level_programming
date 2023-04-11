#!/usr/bin/python3
"""module which inherits from the list class"""


class MyList(list):
    """Class which inherits from the list"""
    def print_sorted(self):
        """This prints a sorted list"""
        print(sorted(self))
