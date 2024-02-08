#!/usr/bin/python3

def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited (directly or indirectly)
    from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if the object is an instance of a class that inherited from the specified class;
        otherwise False.

    Example:
        >>> inherits_from(True, int)
        True
        >>> inherits_from(True, bool)
        True
        >>> inherits_from(True, object)
        True
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class

