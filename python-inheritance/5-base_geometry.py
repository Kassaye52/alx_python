#!/usr/bin/python3
"""
This is a documentation for 6. Rectangle
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
