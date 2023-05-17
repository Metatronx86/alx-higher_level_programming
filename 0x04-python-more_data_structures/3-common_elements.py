#!/usr/bin/python3

def common_elements(set_1, set_2):
    """
    Return the common elements in two sets.

    Args:
        set_1: The first set.
        set_2: The second set.

    Returns:
        The common elements in the two sets.
    """
    if set_1 is None or set_2 is None:
        return None
    return set_1 & set_2

