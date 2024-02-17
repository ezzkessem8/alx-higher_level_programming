import unittest
import os
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestBase(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(
                file.read(), '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}, '
                             '{"x": 0, "width": 2, "id": 2, "height": 4, "y": 0}]')

    def test_load_from_file(self):
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        self.assertEqual(Rectangle.load_from_file(), [])
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles = [r1, r2]
        Rectangle.save_to_file(list_rectangles)
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 2)
        for rect, saved_rect in zip(list_rectangles, rectangles):
            self.assertEqual(rect.to_dictionary(), saved_rect.to_dictionary())

    def test_save_to_file_csv(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as file:
            self.assertEqual(file.read(), '1,10,7,2,8\n2,2,4,0,0\n')

    def test_load_from_file_csv(self):
        try:
            os.remove("Rectangle.csv")
        except FileNotFoundError:
            pass
        self.assertEqual(Rectangle.load_from_file_csv(), [])
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles)
        rectangles = Rectangle.load_from_file_csv()
        self.assertEqual(len(rectangles), 2)
        for rect, saved_rect in zip(list_rectangles, rectangles):
            self.assertEqual(rect.to_dictionary(), saved_rect.to_dictionary())

    def test_draw(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Base.draw([r1, r2], [s1, s2])

    def test_instance_count(self):
        self.assertEqual(Base._Base__nb_objects, 0)
        r1 = Rectangle(10, 7, 2, 8)
        self.assertEqual(Base._Base__nb_objects, 1)
        r2 = Rectangle(2, 4)
        self.assertEqual(Base._Base__nb_objects, 2)
        s1 = Square(5)
        self.assertEqual(Base._Base__nb_objects, 3)
        s2 = Square(7, 9, 1)
        self.assertEqual(Base._Base__nb_objects, 4)

    def test_id_assignment(self):
        r1 = Rectangle(10, 7, 2, 8)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 4)
        self.assertEqual(r2.id, 2)
        s1 = Square(5)
        self.assertEqual(s1.id, 3)
        s2 = Square(7, 9, 1)
        self.assertEqual(s2.id, 4)


if __name__ == '__main__':
    unittest.main()

