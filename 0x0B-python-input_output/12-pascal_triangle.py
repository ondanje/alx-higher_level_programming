#!/usr/bin/python3
"""function that prints pascal triangle"""


def pascal_triangle(n):
    """
    function def pascal_triangle(n): that returns a list of
    lists of integers representing the Pascal’s triangle of n
    """

    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        tri = triangle[-1]
        temp = [1]
        for i in range(len(tri) - 1):
            temp.append(tri[i] + tri[i + 1])
        temp.append(1)
        triangle.append(temp)
    return triangle
