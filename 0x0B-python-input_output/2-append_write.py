#!/usr/bin/python3
""" a function that appends a string at the end of a text file and returns the number of chars added"""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file.

    Args:
        filename (str): The name of the file to append.
        text (str): The string to append.
    Returns:
        The number of chars that was appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
