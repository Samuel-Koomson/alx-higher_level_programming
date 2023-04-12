#!/usr/bin/python3
"""function which inherits from basegeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """method uses rectangle to define geometry"""
    def __init__(self, width, height):
        """this initializes a new rectangle
        """
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
