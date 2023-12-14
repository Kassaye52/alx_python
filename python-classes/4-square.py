#!/usr/bin/python3
"""
This is a documentation for 4. Printing a square
"""
class Square:
    """Class that defines a square by its size with the ability to calculate its area and print itself."""

    def __init__(self, size=0):
        """Initialize the square with an optional size argument.

        Args:
            size (int, optional): The size of the square's side. Defaults to 0.
        
        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square, with checks for integer type and value >= 0.

        Args:
            value (int): The size to set for a side of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character # or an empty line if size is 0."""
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
