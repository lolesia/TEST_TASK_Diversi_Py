from figure import Circle, Square, Rectangle, Triangle


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
        if shape_type == 'Triangle':
            return Triangle(*ShapeInputHandler.triangle_handler(items))
        else:
            raise ValueError(f'Incorrect data input for {shape_type}')

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

    @staticmethod
    def triangle_handler(items):
        return [0, 0, 0, 0, 0, 0]


# print(ShapeInputHandler.handler(input()).output())

