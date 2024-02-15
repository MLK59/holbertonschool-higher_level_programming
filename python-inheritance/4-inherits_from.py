#!/usr/bin/python3

"""
subclass checker
Parameters:
obj (object): The object to check.
cls (class): The specified class to check against.

Returns:
bool: True if obj is an instance of a class that inherited from cls,
False otherwise.
"""


def inherits_from(obj, a_class):
    """
    returns True if obj is an instance of a class that inherited
    from a_class,or if obj is an instance of a_class itself.
    False otherwise.
    """
    if isinstance(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
