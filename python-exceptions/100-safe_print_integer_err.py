#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except IndexError as e:
        sys.stderr.write("Exception: {}".format(e))
        return False
