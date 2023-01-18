#!/usr/bin/python3
""" Read file"""


def read_file(filename=""):
    if filename:
        with open(filename, mode = 'r', encoding="utf-8") as f:
            a = f.read()
            print(a)
