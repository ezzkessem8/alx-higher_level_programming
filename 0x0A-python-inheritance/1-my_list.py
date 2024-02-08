#!/usr/bin/python3
"""
This program creates a class called MyList that inherits of the class List
"""

class MyList(list):
    """
    MyList class extends the built-in list class with additional functionality.
    """

    def print_sorted(self):
        """
        Print the list in sorted order (ascending).

        Example:
            >>> my_list = MyList()
            >>> my_list.append(1)
            >>> my_list.append(4)
            >>> my_list.append(2)
            >>> my_list.append(3)
            >>> my_list.append(5)
            >>> my_list.print_sorted()
            [1, 2, 3, 4, 5]
        """
        sorted_list = sorted(self)
        print(sorted_list)

