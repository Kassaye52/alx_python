#!/usr/bin/python3
""" 0-main """
class Base:
    """
    This is the base class for all models.

    It manages the id attribute in all future classes and avoids duplicating code.

    Attributes:
        __nb_objects (int): A private class attribute that keeps track of the number of objects created.

    Args:
        id (int, optional): An identifier for the object. If not provided, it is auto-generated.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        The constructor for the Base class.

        Args:
            id (int, optional): An identifier for the object. If None, __nb_objects is incremented and used as id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

