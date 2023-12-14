#!/usr/bin/python3
"""
This is a documentation for 4. Printing a square
"""
def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of the specified class.

    Args:
    obj: Any - The object to check.
    a_class: type - The class to compare against.

    Returns:
    bool: True if obj is exactly an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
