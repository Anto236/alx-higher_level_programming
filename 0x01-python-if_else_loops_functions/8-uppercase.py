#!/usr/bin/python3


def uppercase(str):

    for x in str:
        y = ord(x)
        if y >= 97 and y <= 122:
            y -= 32

        y = chr(y)

        print("{}".format(y), end="")

    print()
