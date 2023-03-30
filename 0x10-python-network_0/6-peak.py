#!/usr/bin/python3
""" Finds a peak inside a list """


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): The list of integers to search.

    Returns:
        int: The peak value.

    If list is empty:
        Return 0
    """
    if list_of_integers == []:
        return None

    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
