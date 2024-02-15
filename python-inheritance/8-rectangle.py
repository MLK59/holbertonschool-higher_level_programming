#!/usr/bin/python3

BaseGeometry = __import__("7-base_geometry").BaseGeometry
"""
Rectangle class with width and height
"""


class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        """
        instantiation with width and height
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
