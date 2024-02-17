#!/usr/bin/python3
"""Unit tests for Square class."""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square class."""

    def test_constructor(self):
        """Test if constructor initializes attributes correctly."""
        s = Square(5, 1, 2, 3)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 3)

    def test_str(self):
        """Test string representation of square."""
        s = Square(5, 1, 2, 3)
        self.assertEqual(str(s), "[Square] (3) 1/2 - 5")

    def test_area(self):
        """Test calculation of square's area."""
        s = Square(5)
        self.assertEqual(s.area(), 25)

        s.size = 3
        self.assertEqual(s.area(), 9)

    def test_display(self):
        """Test display of square."""
        s = Square(4)
        expected_output = "####\n####\n####\n####\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            s.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_update(self):
        """Test updating attributes of square."""
        s = Square(5, 1, 2, 3)
        s.update(89)
        self.assertEqual(s.id, 89)

        s.update(89, 2)
        self.assertEqual(s.size, 2)

        s.update(89, 2, 3)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)

        s.update(89, 2, 3, 4)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

        s.update(size=1)
        self.assertEqual(s.size, 1)

        s.update(size=2, x=3)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)

        s.update(y=1, size=2, x=3, id=89)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 1)
        self.assertEqual(s.id, 89)

        s.update(x=1, size=2, y=3)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 3)

    def test_to_dictionary(self):
        """Test conversion to dictionary."""
        s = Square(10, 2, 1, 3)
        expected_dict = {'id': 3, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(s.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()

