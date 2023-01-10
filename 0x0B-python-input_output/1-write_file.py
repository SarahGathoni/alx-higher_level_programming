#!/usr/bin/python3
"""Defines a text files and returns number of characters"""


def write_file(filename="", text=""):
    """Return the number of lines in a text file."""
    lines = 0
    with open(filename) as f:
        for line in f:
            lines += 1
    return lines
