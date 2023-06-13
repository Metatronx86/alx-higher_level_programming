#!/usr/bin/python3
"""
Contains the definition for the Square class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Definition of the Square class that inherits from the Rectangle class"""

    def __init__(self, size):
        """Initializes an instance of the Square class"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Computes the area of the Square"""
        return self.__size ** 2

    def __str__(self):
        """Returns a string representation of an instance of the Square class"""
        return "[{}] {}/{}".format(type(self).__name__, self.__size, self.__size)

