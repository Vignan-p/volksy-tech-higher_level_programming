#!/usr/bin/python3
islower = __import__('7-islower').islower
print("c is {}".format("lower" if islower("c") else "upper"))
print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("! is {}".format("lower" if islower("!") else "upper"))
print("4 is {}".format("lower" if islower("4") else "upper"))
