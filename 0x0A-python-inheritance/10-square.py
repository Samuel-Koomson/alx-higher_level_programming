#!/usr/bin/python3
"""Function defines a rectangle subclass square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """method defines a square"""

    def __init__(self, size):
        """this initialize a new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
