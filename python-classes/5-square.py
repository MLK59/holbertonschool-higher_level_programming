#!/usr/bin/python3

"""class that defines a Square"""


class Square:

    """Initialise the class with a private instance attribute size"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Return the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Check execption tupe and value for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for line in range(self.__size):
                print("#" * self.__size)
