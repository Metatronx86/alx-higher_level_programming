#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
    Print a dictionary with keys sorted in alphabetical order.

    Args:
        a_dictionary: The dictionary to print.

    Returns:
        None
    """
    sorted_keys = sorted(a_dictionary.keys())
    for key in sorted_keys:
        print(key, ":", a_dictionary[key])

