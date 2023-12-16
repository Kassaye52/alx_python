#!/usr/bin/python3
""" 0-main """

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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get or set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get or set the x coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get or set the y coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate the area of the Rectangle instance.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height
    
    def display(self):
        """
        Print the Rectangle instance using the '#' character.
        """
        for _ in range(self.height):
            print("#" * self.width)

    def __str__(self):
        """
        Return the string representation of the Rectangle instance.

        Returns:
            str: A string representation of the rectangle in the format:
                 "[Rectangle] (<id>) <x>/<y> - <width>/<height>"
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
    
    def display(self):
        """
        Print the Rectangle instance using the '#' character, taking into account 'x' and 'y' coordinates.
        """
        print("\n" * self.y, end="")  
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)  
    
    def update(self, *args):
        """
        Update the attributes of the Rectangle instance using no-keyword arguments.

        Args:
            *args: A variable length argument list, where:
                   1st argument is for id
                   2nd argument is for width
                   3rd argument is for height
                   4th argument is for x
                   5th argument is for y
        """
        attr_order = ['id', 'width', 'height', 'x', 'y']
        for attr, value in zip(attr_order, args):
            if hasattr(self, attr):
                setattr(self, attr, value)
                
    def update(self, *args, **kwargs):
        """
        Update the attributes of the Rectangle instance.

        Args:
            *args: A variable length argument list, where:
                   1st argument is for id
                   2nd argument is for width
                   3rd argument is for height
                   4th argument is for x
                   5th argument is for y
            **kwargs: A variable length keyword argument dictionary. Used to update attributes if *args is empty.
        """
        attr_order = ['id', 'width', 'height', 'x', 'y']

        if args:
            for attr, value in zip(attr_order, args):
                if hasattr(self, attr):
                    setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)


