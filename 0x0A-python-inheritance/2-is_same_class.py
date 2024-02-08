#!/usr/bin/python3

def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if the object is exactly an instance of the specified class, False otherwise.

    Example:
        >>> is_same_class(1, int)
        True
        >>> is_same_class(1, float)
        False
        >>> is_same_class(1, object)
        False
    """
    return type(obj) is a_class

