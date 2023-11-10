from abc import ABC, abstractmethod
from math import pi


class Figure(ABC):
    """Abstract base class representing a geometric figure."""

    def __init__(self, x1, y1, x2, y2, side):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.side = side

    @abstractmethod
    def output(self):
        pass


class Square(Figure):
    """
    A class representing a Square that inherits from Figure.
    """

    def __init__(self, side):
        super().__init__(None, None, None, None, side)

    def output(self):
        """
        Calculates and returns the perimeter and area of the square.

        Returns:
            str: A string containing information about the Square's perimeter and area.
        Raises:
            ValueError: If the side is not positive integer .
        """
        if isinstance(self.side, int) and self.side > 0:
            perimeter = self.side * 4
            area = self.side ** 2
            return f"Square Perimeter {perimeter} Area {area}"
        else:
            raise ValueError('Side must be integer positive')


class Rectangle(Figure):
    """
    A class representing a Rectangle that inherits from Figure.
    """

    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2, None)

    def output(self):
        """
        Calculates and returns the perimeter and area of the rectangle.

        Returns:
            str: A string containing information about the rectangle's perimeter and area.
        Raises:
            ValueError: If the coordinates is not integer.
        """
        if all(isinstance(val, int) for val in [self.x1, self.y1, self.x2, self.y2]):
            side1 = abs(self.x1 - self.x2)
            side2 = abs(self.y1 - self.y2)
            perimeter = (side1 + side2) * 2
            area = side1 * side2
            return f"Rectangle Perimeter {perimeter} Area {area}"
        else:
            raise ValueError('All coordinates must be integer')


class Circle(Figure):
    """
    A class representing a Circle that inherits from Figure.
    """
    def __init__(self, side):
        super().__init__(None, None, None, None, side)

    def output(self):
        """
        Calculates and returns the perimeter and area of the circle.

        Returns:
            str: A string containing information about the circle's perimeter and area.
        Raises:
            ValueError: If the radius is not a positive integer.
        """
        if isinstance(self.side, int) and self.side > 0:
            perimeter = 2 * pi * self.side
            area = pi * self.side**2
            return f"Circle Perimeter {perimeter} Area {area}"
        else:
            raise ValueError('Radius must be integer positive')


class ShapeInputHandler:
    """
    Class ShapeInputHandler is responsible for processing incoming
    data and distribution by type of geometric figure

    """

    @staticmethod
    def handler(str_input):
        """
        Parses a string input and returns a shape object.

        Args:
            str_input: A string containing the shape type and parameters.

        Returns:
            A shape object, or None if the input is invalid.

        Raises:
            ValueError: If the input is invalid.
        """
        items = str_input.split()
        shape_type = items[0]

        if shape_type == 'Square':
            return Square(ShapeInputHandler.square_handler(items))
        if shape_type == 'Rectangle':
            return Rectangle(*ShapeInputHandler.rectangle_handler(items))
        if shape_type == 'Circle':
            return Circle(ShapeInputHandler.circle_handler(items))
        else:
            raise ValueError('Incorrect data input')

    @staticmethod
    def square_handler(items):
        """
        parses data from a string to calculate
        the area and perimeter of a square

        """

        side = int(items[5])

        return side

    @staticmethod
    def rectangle_handler(items):
        """
        parses data from a string to calculate
        the area and perimeter of a rectangle

        """

        x1, y1 = int(items[2]), int(items[3])
        x2, y2 = int(items[5]), int(items[6])

        return x1, y1, x2, y2

    @staticmethod
    def circle_handler(items):
        """
        parses data from a string to calculate
        the area and perimeter of a circle

        """

        side = int(items[5])

        return side


# print(ShapeInputHandler.handler(input()).output())





