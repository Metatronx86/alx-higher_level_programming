#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Return the key with the biggest integer value.

    Args:
        a_dictionary: The dictionary to find the best score from.

    Returns:
        The key with the biggest integer value, or None if no score found.
    """
    best_key = None
    best_value = float('-inf')
    for key, value in a_dictionary.items():
        if isinstance(value, int) and value > best_value:
            best_key = key
            best_value = value
    return (best_key)

