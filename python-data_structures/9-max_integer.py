#!/usr/bin/python3
def max_integer(my_list=[]):
    j = 0
    if len(my_list) < 0:
        return None
    else:
        for i in my_list:
            if i < j:
                continue
            if i > j:
                j = i
        return j
            
