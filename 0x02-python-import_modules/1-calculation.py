#!/usr/bin/python3
# 1-calculation.py

if __name__ == "__main__":
    """This program does basic maths operations. addition, subtraction,
    multiplication and division using the values  of 10 and 5, and makes 
    use of imported functions in the calculator_1 module"""
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
