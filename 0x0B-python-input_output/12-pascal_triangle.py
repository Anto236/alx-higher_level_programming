#!/usr/bin/python3
"""module pascal triangle"""


def pascal_triangle(n):
    """returns empty list if n<=0"""

    if n <= 0:
        return []

    """define the triangle"""
    triangle = [[1]]
    """loop while appending the integers"""
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle
