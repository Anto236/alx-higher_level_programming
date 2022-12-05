#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):

    if tuple_a is None or tuple_a is not None:
        if len(tuple_a) == 0:
            atup = (0, 0)
        elif len(tuple_a) == 1:
            atup = (tuple_a[0], 0)
        else:
            atup = (tuple_a[0], tuple_a[1])

    if tuple_b is None or tuple_b is not None:
        if len(tuple_b) == 0:
            btup = (0, 0)
        elif len(tuple_b) == 1:
            btup = (tuple_b[0], 0)
        else:
            btup = (tuple_b[0], tuple_b[1])

    sumtup = (atup[0] + btup[0], atup[1] + btup[1])

    return sumtup
