#!/usr/bin/python3
"""
Module to add two integers
"""

def add_integer(a, b=98):
    """
    Adds two integers

    Args:
    - a: first integer
    - b: second integer (default is 98)

    Returns:
    - the addition of a and b

    Raises:
    - TypeError: If a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
