#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    r = 0
    try:
        for i in range(0, x):
            print("{:d}".format(my_list[i]), end = "")
            r = r + 1
        return r
    except:
        pass
