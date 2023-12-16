#!/usr/bin/python3
""" 0-main """
# Assuming models/base.py contains the Base class as previously defined

from .base import Base

class Rectangle(Base):
    """
    Represents a rectangle.

    Inherits from Base class and adds specific attributes for rectangle management.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x coordinate. Defaults to 0.
            y (int, optional): The y coordinate. Defaults to 0.
            id (int, optional): The id of the rectangle. If None, Base class will auto-assign.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get or set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value  # Add validation as needed

    @property
    def height(self):
        """Get or set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value  # Add validation as needed

    @property
    def x(self):
        """Get or set the x coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value  # Add validation as needed

    @property
    def y(self):
        """Get or set the y coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value  # Add validation as needed
