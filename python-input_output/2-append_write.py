#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """Append to a file
    Args:
        filename: name of the file
        text: text to append
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
