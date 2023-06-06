#!/usr/bin/python3
"""
Module to find the maximum integer in a list.
"""


def max_integer(list=[]):
    """
    Function to find and return the maximum integer in a list of integers.
    If the list is empty, the function returns None.
    """
    if len(list) == 0:
        return None
    maximum = list[0]
    for num in list:
        if num > maximum:
            maximum = num
    return maximum

