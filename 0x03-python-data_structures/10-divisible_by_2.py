#!/usr/bin/python3


def divisible_by_2(my_list=[]):

    nlist = my_list.copy()
    y = 0

    for x in my_list:
        if x % 2 == 0:
            nlist[y] = True

        else:
            nlist[y] = False
        y += 1

    return nlist
