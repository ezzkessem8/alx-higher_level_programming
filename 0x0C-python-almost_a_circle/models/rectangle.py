#!/usr/bin/python3
"""Module defining Rectangle class."""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class, inherits from Base.

    Attributes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x (int): x coordinate of the rectangle.
        y (int): y coordinate of the rectangle.
        id (int): Unique identifier of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize Rectangle object.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): x coordinate. Defaults to 0.
            y (int, optional): y coordinate. Defaults to 0.
            id (int, optional): Unique identifier. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the rectangle with '#' characters."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return string representation of the Rectangle instance."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """
        Update attributes of the Rectangle.

        Args:
            *args: Non-keyword arguments representing attribute values
            **kwargs: Keyword arguments representing attribute key-value pairs
        """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

