#!/usr/bin/python3

"""Base class module.
This module contains the Base class.
"""


class Base:
    """Base class for all other classes in the project.

    Attributes:
        __nb_objects (int, private): Counts the number of created instances.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id (int, optional): The ID of the instance. If None, a unique ID is assigned.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
