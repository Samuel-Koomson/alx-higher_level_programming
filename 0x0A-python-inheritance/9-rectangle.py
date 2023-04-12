#!/usr/bin/python3
"""function defines a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """method represents a rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """ this initialises a new Rectangle
        width(int): Width of the rectangle
        height(int): Height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """method returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """method returns the print() and str() functions  of a Rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
