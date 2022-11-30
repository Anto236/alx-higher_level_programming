#!/usr/bin/python3
def uppercase(str):
    for i in str:
        check = ord(i)
        if check >= 97 and check <= 122:
            check = check - 32
            i = chr(check)
        print("{}".format(i))
    print()
