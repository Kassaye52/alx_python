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
    """Rectangle class inherited from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize the rectangle."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize the square with size as both the width and height."""
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self._Rectangle__width * self._Rectangle__height  # Accessing the private attribute from the parent class

    def __str__(self):
        """Return the square description."""
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__width)


