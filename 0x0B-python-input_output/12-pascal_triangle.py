#!/usr/bin/python3
"""Pascal's triangle"""


def pascal_triangle(n):
    """Pascal's triangle generator"""
    if n <= 0:
        return []
    triangle = []
    my_list = []
    for i in range(1, n):
        l, r = -1, 0
        prev_list = my_list
        my_list = []
        if i == 1:
            my_list = [1]
            triangle.append(my_list)
            continue
        for j in range(i):
            if r == i - 1:
                my_list.append(prev_list[l])
            elif l == -1:
                my_list.append(prev_list[r])
            else:
                my_list.append(prev_list[l] + prev_list[r])
            l += 1
            r += 1
        triangle.append(my_list)
    return triangle
