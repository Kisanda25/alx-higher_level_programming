#!/usr/bin/python3
"""a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ a square."""

    def __init__(self, size):
        """Initializes a new square.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
