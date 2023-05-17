#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
    Return the difference between two sets.

    Args:
        set_1: The first set.
        set_2: The second set.

    Returns:
        The difference between the two sets.
    """
    if set_1 is None or set_2 is None:
        return None
    return set_1 ^ set_2

