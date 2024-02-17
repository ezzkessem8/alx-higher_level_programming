#!/usr/bin/python3
"""Unit tests for Rectangle class."""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class."""

    def test_constructor(self):
        """Test if constructor initializes attributes correctly."""
        r = Rectangle(10, 5, 1, 2, 3)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 3)

    def test_width(self):
        """Test getter and setter for width attribute."""
        r = Rectangle(10, 5)
        r.width = 15
        self.assertEqual(r.width, 15)

        with self.assertRaises(TypeError):
            r.width = "invalid"

        with self.assertRaises(ValueError):
            r.width = -10

    def test_height(self):
        """Test getter and setter for height attribute."""
        r = Rectangle(10, 5)
        r.height = 8
        self.assertEqual(r.height, 8)

        with self.assertRaises(TypeError):
            r.height = "invalid"

        with self.assertRaises(ValueError):
            r.height = -5

    def test_x(self):
        """Test getter and setter for x attribute."""
        r = Rectangle(10, 5)
        r.x = 3
        self.assertEqual(r.x, 3)

        with self.assertRaises(TypeError):
            r.x = "invalid"

        with self.assertRaises(ValueError):
            r.x = -2

    def test_y(self):
        """Test getter and setter for y attribute."""
        r = Rectangle(10, 5)
        r.y = 4
        self.assertEqual(r.y, 4)

        with self.assertRaises(TypeError):
            r.y = "invalid"

        with self.assertRaises(ValueError):
            r.y = -3

    def test_area(self):
        """Test calculation of rectangle's area."""
        r = Rectangle(10, 5)
        self.assertEqual(r.area(), 50)

        r.width = 3
        r.height = 7
        self.assertEqual(r.area(), 21)

    def test_display(self):
        """Test display of rectangle."""
        r = Rectangle(4, 6)
        expected_output = "####\n####\n####\n####\n####\n####\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            r.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_str(self):
        """Test string representation of rectangle."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update(self):
        """Test updating attributes of rectangle."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)
        
        r.update(89, 2)
        self.assertEqual(r.width, 2)

        r.update(89, 2, 3)
        self.assertEqual(r.height, 3)

        r.update(89, 2, 3, 4)
        self.assertEqual(r.x, 4)

        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.y, 5)

        r.update(width=1)
        self.assertEqual(r.width, 1)

        r.update(width=2, x=3)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.x, 3)

        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.id, 89)

        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.width, 4)


if __name__ == '__main__':
    unittest.main()

