#!/usr/bin/python3

if __name__ == "__main__":
    """prints the result of the addition of all arguments"""
    from sys import argv
    from calculator_1 import add, sub, mul, div
    arg_num = len(argv) - 1
    operators = ["+", "-", "*", "/"]

    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])

    if arg_num < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    elif operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
    else:
        print("{} {} {} = {}".format(a, operator, b, add(a, b)))
