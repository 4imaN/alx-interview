#!/usr/bin/python3
"""
Module 0-pascal_triangle
Contains function pascal_triangle(n)
"""

def pascal_triangle(n):
    """
    Pascal's triangle solver.
    
    Args:
        n (int): The number of rows of the triangle
        
    Returns:
        list: A list of lists of integers representing Pascal's triangle
    """
    if n <= 0:
        return []
    
    triangle = [[1]]
    
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    
    return triangle