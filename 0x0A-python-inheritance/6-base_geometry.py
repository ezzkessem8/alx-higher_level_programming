#!/usr/bin/python3

class BaseGeometry:
    """
    BaseGeometry class represents a base geometry class.
    """

    def area(self):
        """
        Compute the area of the geometry.

        Raises:
            Exception: Always raises an Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

