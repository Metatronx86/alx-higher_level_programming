#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """
    Delete entries from a dictionary based on a specified value.

    Args:
        a_dictionary (dict): The dictionary to be modified.
        value: The value to be deleted from the dictionary.

    Returns:
        dict: The modified dictionary after deleting entries with the specified value.

    """
    keys_to_delete = []
    for key, val in a_dictionary.items():
        if val == value:
            keys_to_delete.append(key)
    for key in keys_to_delete:
        del a_dictionary[key]
    return a_dictionary

