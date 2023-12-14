#!/usr/bin/python3
"""
This is a documentation for 5. Integer validator
"""

class BaseGeometry:
    """BaseGeometry class for handling geometrical operations and validation."""

    def area(self):
        """Raise an Exception with the message for unimplemented method."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the integer value.

        Args:
        name (str): The name of the variable.
        value (int): The value associated with the name.

        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize the rectangle with width and height.

        Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

        Raises:
        TypeError: If width or height is not an integer.
        ValueError: If width or height is less or equal to 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
