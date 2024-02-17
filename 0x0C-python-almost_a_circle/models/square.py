#!/usr/bin/python3
"""Module defining Square class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class, inherits from Rectangle.

    Attributes:
        size (int): Size of the square.
        x (int): x coordinate of the square.
        y (int): y coordinate of the square.
        id (int): Unique identifier of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize Square object.

        Args:
            size (int): Size of the square.
            x (int, optional): x coordinate. Defaults to 0.
            y (int, optional): y coordinate. Defaults to 0.
            id (int, optional): Unique identifier. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return string representation of the Square instance."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size
        )

    def update(self, *args, **kwargs):
        """
        Update attributes of the square.

        Args:
            *args (tuple): List of arguments.
            **kwargs (dict): Dictionary of keyword arguments.
        """
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Return dictionary representation of the square.

        Returns:
            dict: Dictionary containing attributes of the square.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

