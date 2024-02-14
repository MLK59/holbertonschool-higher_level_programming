#!/usr/bin/python3

"""
subclass checker
Parameters:
obj (object): The object to check.
cls (class): The specified class to check against.

Returns:
bool: True if obj is an instance of a class that inherited from cls, False otherwise.
"""


def inherits_from(obj, a_class):
    """returns subclass yes"""
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
