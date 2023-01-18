#!/usr/bin/python3
"""write a file"""


def write_file(filename="", text=""):
    """Write"""
    if filename:
        with open(filename, mode='w', encoding="utf-8") as f:
            return (f.write(text))
