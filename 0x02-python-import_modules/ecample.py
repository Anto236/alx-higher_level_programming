#!/usr/bin/python3
import sys
print("the arguments is:", len(sys.argv))
print("the argument is:", (sys.argv))
count = len(sys.argv)
for i in range(count):
    print("index{}: {}".format((i + 1), sys.argv[i + 1]))
