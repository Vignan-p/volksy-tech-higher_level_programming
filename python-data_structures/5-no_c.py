#!/usr/bin/python3
def no_c(my_string):
    copy = []
    for x in my_string:
        if x != "c" or x != "C":
            copy.append(x)
    return ("".join(copy))
