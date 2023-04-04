#!/usr/bin/python3
"""A module which contains a class rectangle"""


class Rectangle:
    """ Module defines a rectangle class
    The module contains two attributes width and height which are private
    The attribute values must accept integers only.
    TypeError will be raised is values are not integers while ValueError will be raised if values are less than 0.
    Two new attributes area and perimeter are added.
    """
    number_of_instances = 0
    print_symbol = '#'
    
    def __init__(self, width=0, height=0):
        """This method initializes height and width attributes to 0
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
    
    def area(self):
        """method returns the area of the triangle"""
        return self.__width * self.__height
        
    def perimeter(self):
        """method returns the perimeter of the triangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))
    
    def __str__(self):
        """function for prints a rectangle using the #"""
        if self.width == 0 or self.height == 0:
            return rectangle
        
        for x in range(self.height):
            rectangle += ("#" * self.width) + "\n"
        return rectangle[:-1]
    
    def __repr__(self):
        return "Rectangle ({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """delete and output a message after an instance is removed"""
        print("Bye rectangle ...")
        Rectangle.number_of_instances -= 1
