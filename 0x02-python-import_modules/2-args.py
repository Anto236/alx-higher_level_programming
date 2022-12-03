#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1
    print("{} ".format(count), end="")
    if count == 0:
        print("arguments")
    elif count == 1:
        print("argument:")
    else:
        print("arguments:")
    for i in range(count):
        print("{}: {}".format((i + 1), sys.argv[i + 1]))
