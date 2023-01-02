#!/usr/bin/python3
def print_last_digit(number):
    a = number % 10
    if number == 0:
        return 0
    elif number > 0:
        return a
    elif number < 0:
        a = 10 - a
        return a
