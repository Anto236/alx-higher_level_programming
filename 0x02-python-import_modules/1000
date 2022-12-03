#!/usr/bin/python3

if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    if (len(argv) - 1) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    x = argv[2]
    b = int(argv[3])

    if x == "+":
        operation = add(a, b)

    elif x == "-":
        operation = sub(a, b)

    elif x == "*":
        operation = mul(a, b)

    elif x == "/":
        operation = div(a, b)

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = {}".format(a, x, b, operation))
