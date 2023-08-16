#!/usr/bin/python3
"""returns a list of lists of integers"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        shape = triangles[-1]
        temp = [1]
        for i in range(len(shape) - 1):
            temp.append(shape[i] + shape[i + 1])
        temp.append(1)
        triangles.append(temp)
    return triangles
