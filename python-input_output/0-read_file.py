#!/usr/bin/python3

"""Read file"""


def read_file(filename=""):
    """Read
    Args:
        filename: name of the file
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
