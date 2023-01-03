#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    l = len(sys.argv)
    if l <= 1:
        print("0 arguments.")
    else:
        print("{:d} arguments:".format(l))
    for i in range(1, l):
        print("{:d}: {:s}".format(i, sys.argv[i]))
