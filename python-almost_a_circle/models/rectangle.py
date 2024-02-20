#!/usr/bin/python3

# Import the Base class from the base module within the models package
from .base import Base


class Rectangle(Base):  # Rectangle inherits from Base
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x coordinate of the rectangle. Defaults to 0.
            y (int, optional): The y coordinate of the rectangle. Defaults to 0.
            id (int, optional): An identifier for the rectangle. Defaults to None, which triggers automatic id assignment.
        """
        # Call the constructor of the Base class, enabling automatic id assignment or using the provided id
        super().__init__(id)
        # Set instance attributes with the provided values, using setters for validation
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Getter for the width attribute
    @property
    def width(self):
        return self.__width

    # Setter for the width attribute, includes a placeholder for validation logic
    @width.setter
    def width(self, value):
        # Validation logic could go here (e.g., check if value is an int and greater than 0)
        self.__width = value

    # Getter for the height attribute
    @property
    def height(self):
        return self.__height

    # Setter for the height attribute, includes a placeholder for validation logic
    @height.setter
    def height(self, value):
        # Validation logic could go here
        self.__height = value

    # Getter for the x attribute
    @property
    def x(self):
        return self.__x

    # Setter for the x attribute, includes a placeholder for validation logic
    @x.setter
    def x(self, value):
        # Validation logic could go here
        self.__x = value

    # Getter for the y attribute
    @property
    def y(self):
        return self.__y

    # Setter for the y attribute, includes a placeholder for validation logic
    @y.setter
    def y(self, value):
        # Validation logic could go here
        self.__y = value
