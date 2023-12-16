#!/usr/bin/python3
""" 0-main """

# Assuming models/rectangle.py contains the Rectangle class as previously defined

from .rectangle import Rectangle

class Square(Rectangle):
    """
    Represents a square, which is a special case of a rectangle.

    Inherits from Rectangle, with width and height being equal.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square's sides.
            x (int, optional): The x coordinate. Defaults to 0.
            y (int, optional): The y coordinate. Defaults to 0.
            id (int, optional): The id of the square. If None, Base class will auto-assign.
        """
        super().__init__(size, size, x, y, id)  # Width and height are both set to size

    def __str__(self):
        """
        Return the string representation of the Square instance.
        """
    @property
    def size(self):
        """
        Get the size of the square (width and height are the same).

        Returns:
            int: The size of the square.
        """
        return self.width  # Since width and height are the same

    @size.setter
    def size(self, value):
        """
        Set the size of the square, which updates both width and height.

        Args:
            value (int): The new size of the square.
        """
        self.width = value  
        self.height = value  
