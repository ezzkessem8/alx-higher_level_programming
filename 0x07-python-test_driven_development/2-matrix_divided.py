#!/usr/bin/python3
"""
Module to divide all elements of a matrix
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number

    Args:
    - matrix: a list of lists of integers or floats
    - div: a number (integer or float) to divide the elements by

    Returns:
    - a new matrix with elements rounded to 2 decimal places

    Raises:
    - TypeError: If matrix is not a list of lists of integers/floats
                If each row of the matrix does not have the same size
                If div is not a number
    - ZeroDivisionError: If div is equal to 0
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return result_matrix
