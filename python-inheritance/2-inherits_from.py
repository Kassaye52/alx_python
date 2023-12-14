#!/usr/bin/python3
"""
This is a documentation for 2. Only sub class of
"""
def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited from the specified class.

    Args:
    obj: Any - The object to check.
    a_class: type - The class to compare against.

    Returns:
    bool: True if obj is an instance of a subclass of a_class, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
