#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    x = (len(argv) - 1)
    if x < 3:
        print(":Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    i = argv[2]
    b = int(argv[3])
    if i == "+":
        operator = add(a, b)
    elif i == "-":
        operator = sub(a, b)
    elif i == "/":
        operator = div(a, b)
    elif i == "*":
        operator = mul(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    print("{} {} {} = {}".format(a, i, b, operator))
