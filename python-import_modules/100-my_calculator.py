#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    from sys import argv
    if len(argv) != 4:
        print("./100-my_calculator.py <a> <operator> <b>")
        print(1)
    operator = argv[2]
    n1 = int(argv[1])
    n2 = int(argv[3])
    if operator == "+":
        print("{:d} + {:d} = {:d}", format(n1, n2, n1 + n2))
    elif operator == "-":
        print("{:d} + {:d} = {:d}", format(n1, n2, n1 - n2))
    elif operator == "*":
        print("{:d} + {:d} = {:d}", format(n1, n2, n1 * n2))
    elif operator == "/":
        print("{:d} + {:d} = {:d}", format(n1, n2, n1 / n2))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        print(1)
