#!/usr/bin/python3

def weight_average(my_list=[]):
    """
    Calculate the weighted average of a list of tuples.

    Args:
        my_list (list): The list of tuples containing values and their corresponding weights.

    Returns:
        float: The weighted average.

    """
    new_list = []
    total_weight = 0

    if len(my_list) == 0:
        return 0

    for item in my_list:
        new_list.append(item[0] * item[1])
        total_weight += item[1]

    return sum(new_list) / total_weight

