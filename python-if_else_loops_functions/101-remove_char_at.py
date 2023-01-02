#!/usr/bin/python3
def remove_char_at(str, n):
    s = " "
    temp = list(str)
    temp[n] = s
    str = "".join(temp)
    return str
