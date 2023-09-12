#!/usr/bin/python3
"""a function that writes a string to a text file and returns the numb of chars written"""


def write_file(filename="", text=""):
    """Writes to a text file."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
