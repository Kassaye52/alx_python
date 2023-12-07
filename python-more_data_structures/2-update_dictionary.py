def update_dictionary(a_dictionary, key, value):
    """
    Update or add a key-value pair in a dictionary.

    :param a_dictionary: dict - The dictionary to be updated.
    :param key: str - The key to update or add.
    :param value: Any - The value to be associated with the key.
    """
    # Update the dictionary. This will either replace the value for an existing key,
    # or add the key-value pair if the key does not exist.
    a_dictionary[key] = value

