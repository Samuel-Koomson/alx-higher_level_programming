#!/usr/bin/python3
"""A module which contains a class rectangle"""


class Rectangle:
    """ Module defines a rectangle class
    The module contains two attributes width and height which are private
    The attribute values must accept integers only.
    TypeError will be raised is values are not integers while ValueError 
    will be raised if values are less than 0
    """
    def __init__(self, width=0, height=0):
        """This method initializes height and width attributes to 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """function for accessing width"""
        return self.__width

    @width.setter
    def width(self, value):
        """function sets a value to width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """function for accessing height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """function set a value to height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

