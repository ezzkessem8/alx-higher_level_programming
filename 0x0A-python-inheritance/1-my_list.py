#!/usr/bin/python3
"""Module for MyList class."""


class MyList(list):
    """A class inheriting from list with additional functionality."""

    def print_sorted(self):
        """Print the list in ascending order."""
        print(sorted(self))
