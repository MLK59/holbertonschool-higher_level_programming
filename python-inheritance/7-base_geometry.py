#!/usr/bin/python3

"""
class with area method and integer validator method
"""


class BaseGeometry:
    """
    instance of geometry class
    """
    def __init__(self):
        """
        initialize class
        """
        pass

    def area(self):
        """
        raises exception because it is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates an integer to be greater than 0 and an integer
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
