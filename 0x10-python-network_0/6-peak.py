#!/usr/bin/python3
def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers using a binary search-like approach.

    Args:
        list_of_integers (list): List of unsorted integers.

    Returns:
        int: The peak element found in the list.

    Note:
        There may be more than one peak in the list.
    """
    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        # Compare the middle element with its neighbors
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid  # The peak is in the left half (inclusive)
        else:
            left = mid + 1  # The peak is in the right half

    return list_of_integers[left]


