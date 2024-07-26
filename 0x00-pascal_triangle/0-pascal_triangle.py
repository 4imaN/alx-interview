#!/usr/bin/python3



def pascal_triangle(n):
    if n <= 0:
        return []
    my_list, temp, r = [], [], 0
    for i in range(n):
        while r <= i:
            temp.append(int(combination(i, r)))
            r += 1
        my_list.append(temp)
        temp = []
        r = 0
    return my_list
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def combination(n, r):
    num = factorial(n)
    den = factorial(n - r) * factorial(r)
    return num / den