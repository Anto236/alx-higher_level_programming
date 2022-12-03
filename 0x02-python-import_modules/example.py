#!/usr/bin/pythoni3
if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1
    print("Number of students is {}".format(count))
    if count == 0:
        print("Find students")
    else:
        if count == 1:
            print("{}: {}".format(count, sys.argv[1]))
        else:
            if count > 1:
                for i in range(count):
                    print("{}: {}".format((i + 1), (sys.argv[i + 1])))
