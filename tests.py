import unittest
from figure import Square, Rectangle, Circle, ShapeInputHandler
from math import pi


class TestSquare(unittest.TestCase):

    def test_output_square(self):
        side = 5
        square = Square(side)
        test_perimeter = side * 4
        test_area = side ** 2
        self.assertEqual(square.output(), f"Square Perimeter {test_perimeter} Area {test_area}")

    def test_output_square_integer_negative(self):
        side = -5
        with self.assertRaises(ValueError):
            square = Square(side)
            square.output()

    def test_output_square_not_integer(self):
        side = 'a'
        with self.assertRaises(ValueError):
            square = Square(side)
            square.output()


class TestRectangle(unittest.TestCase):

    def test_output_rectangle(self):
        x1, y1 = 5, 10
        x2, y2 = 6, 8
        rectangle = Rectangle(x1, y1, x2, y2)
        side1 = abs(x1 - x2)
        side2 = abs(y1 - y2)
        test_perimeter = (side1 + side2) * 2
        test_area = side1 * side2
        self.assertEqual(rectangle.output(), f"Rectangle Perimeter {test_perimeter} Area {test_area}")

    def test_output_rectangle_not_integer(self):
        x1, y1 = 5, 'r'
        x2, y2 = 'q', 5
        with self.assertRaises(ValueError):
            rectangle = Rectangle(x1, y1, x2, y2)
            rectangle.output()


class TestCircle(unittest.TestCase):

    def test_output_circle(self):
        side = 3
        circle = Circle(side)
        test_perimeter = 2 * pi * side
        test_area = pi * side ** 2
        self.assertEqual(circle.output(), f"Circle Perimeter {test_perimeter} Area {test_area}")

    def test_output_circle_integer_negative(self):
        side = -3
        with self.assertRaises(ValueError):
            circle = Square(side)
            circle.output()


class TestShapeInputHandler(unittest.TestCase):
    def test_square_creation(self):
        shape_input = "Square TopRight 1 1 Side 1"
        square = ShapeInputHandler.handler(shape_input)
        self.assertIsInstance(square, Square)
        self.assertEqual(square.side, 1)

    def test_rectangle_creation(self):
        shape_input = "Rectangle TopRight 2 2 BottomLeft 1 1"
        rectangle = ShapeInputHandler.handler(shape_input)
        self.assertIsInstance(rectangle, Rectangle)
        self.assertEqual(rectangle.x1, 2)
        self.assertEqual(rectangle.y1, 2)
        self.assertEqual(rectangle.x2, 1)
        self.assertEqual(rectangle.y2, 1)

    def test_circle_creation(self):
        shape_input = "Circle Center 1 1 Radius 2"
        circle = ShapeInputHandler.handler(shape_input)
        self.assertIsInstance(circle, Circle)
        self.assertEqual(circle.side, 2)

    def test_invalid_input(self):
        shape_input = "Triangle 3 4 5"
        with self.assertRaises(ValueError):
            ShapeInputHandler.handler(shape_input)
