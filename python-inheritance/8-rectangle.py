#!/usr/bin/python3
# Import the BaseGeometry class from the 7-base_geometry module.
BaseGeometry = __import__("7-base_geometry").BaseGeometry

"""
This module defines the Rectangle class which inherits from BaseGeometry.
It is used to represent a rectangle with a specific width and height.
"""


class Rectangle(BaseGeometry):
    """
    A class used to represent a Rectangle, inheriting from BaseGeometry.

    Attributes:
    __width (int): The width of the rectangle, a private instance attribute.
    __height (int): The height of the rectangle, a private instance attribute.
    """

    def __init__(self, width, height):
        """
        Initialize a new Rectangle instance.

        Parameters:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

        The constructor uses the integer_validator method from the BaseGeometry
        superclass to validate that both the width and height are positive integers.
        """

        # Validate and set the width of the rectangle.
        super().integer_validator("width", width)
        self.__width = width

        # Validate and set the height of the rectangle.
        super().integer_validator("height", height)
        self.__height = height
