#!/usr/bin/python3
"""Base Module."""


class Base:
    """Base Class."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of list_dictionaries."""
        import json
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return list of dictionaries represented by json_string."""
        import json
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @classmethod
    def load_from_file(cls):
        """Return list of instances from a JSON file."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                data = file.read()
                list_dicts = cls.from_json_string(data)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write CSV representation of list_objs to a file."""
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as file:
            if list_objs is not None:
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        file.write("{},{},{},{},{}\n".format(obj.id, obj.width, obj.height, obj.x, obj.y))
                    elif cls.__name__ == "Square":
                        file.write("{},{},{},{}\n".format(obj.id, obj.size, obj.x, obj.y))

    @classmethod
    def load_from_file_csv(cls):
        """Return list of instances from a CSV file."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as file:
                instances = []
                for line in file:
                    data = line.strip().split(',')
                    if cls.__name__ == "Rectangle":
                        instance = cls(int(data[1]), int(data[2]), int(data[3]), int(data[4]), int(data[0]))
                    elif cls.__name__ == "Square":
                        instance = cls(int(data[1]), int(data[2]), int(data[3]), int(data[0]))
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and squares using Turtle graphics."""
        import turtle

        def draw_rectangle(rect):
            turtle.penup()
            turtle.goto(rect.x, rect.y)
            turtle.pendown()
            turtle.setheading(0)
            for _ in range(2):
                turtle.forward(rect.width)
                turtle.right(90)
                turtle.forward(rect.height)
                turtle.right(90)

        def draw_square(sq):
            turtle.penup()
            turtle.goto(sq.x, sq.y)
            turtle.pendown()
            turtle.setheading(0)
            for _ in range(4):
                turtle.forward(sq.size)
                turtle.right(90)

        turtle.speed(0)
        for rect in list_rectangles:
            draw_rectangle(rect)
        for sq in list_squares:
            draw_square(sq)
        turtle.exitonclick()

