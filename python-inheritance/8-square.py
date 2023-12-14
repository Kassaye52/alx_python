#!/usr/bin/python3
"""
This is a documentation for 8. Square #1
"""
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
        self.__size = size  


