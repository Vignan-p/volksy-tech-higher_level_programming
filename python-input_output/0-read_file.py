#!/usr/bin/python3
""" Read file"""


def read_file(filename=""):
    """ read a file"""
    if filename:
        with open(filename, mode = 'r', encoding="utf-8") as f:
            for line in f:
                print(line, end="")
