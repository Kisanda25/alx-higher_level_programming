#!/usr/bin/python3
"""Definition of class called Square"""

class Square:
"""This is the Square class"""
    def __init__(self, size=0):
        """
        Initializes a Square instance.
        
        Args:
            size (int): The size of the square's sides.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size
