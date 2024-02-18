#!/usr/bin/python3

"""Write to a file"""


def write_file(filename="", text=""):
    """Write to a file
    Args:
        filename: name of the file
        text: text to write
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
