#!/usr/bin/python3
"""
This is a documentation for 2. Area of a square
"""
class Square:
    """Class that defines a square with a private size attribute and a method to calculate its area."""

    def __init__(self, size=0):
        """Initialize the square with a specific size.

        Args:
        size (int): The size of a side of the square.

        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size
