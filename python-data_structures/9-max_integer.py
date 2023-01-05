#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 0:
        return None
    j = mylist[0]
    else:
        for i in my_list:
            if i < j:
                continue
            elif i > j:
                j = i
        return j
