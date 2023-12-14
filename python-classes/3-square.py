#!/usr/bin/python3
"""
This is a documentation for 3. Access and update private attribute
"""
class Square:
    """Class that defines a square with a private size attribute, including a property getter and setter."""

    def __init__(self, size=0):
        """Initialize the square with a specific size.

        Args:
        size (int): The size of a side of the square.
        """
        self.size = size  # Note that this will call the size setter

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
        value (int): The size to set for a side of the square.

        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size
