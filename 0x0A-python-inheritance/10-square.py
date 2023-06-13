#!/usr/bin/python3
"""
Definition of the Square class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Definition of the Square class"""
    def __init__(self, size):
        """Instantiation with size"""
        self.__size = size
        super().__init__(self.__size, self.__size)

