#!/usr/bin/python3
"""Function defines a class BaseGeometry"""


class BaseGeometry:
    """Base geometry class definition"""

    def area(self):
        """method unimplemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method validates value as an integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
