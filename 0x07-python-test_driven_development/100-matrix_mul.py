#!/usr/bin/python3

"""
Defines a function for matrix multiplication.
"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    Raises:
        TypeError: If either m_a or m_b is not a list of lists of ints/floats.
        TypeError: If either m_a or m_b is empty.
        TypeError: If either m_a or m_b has rows of different sizes.
        ValueError: If m_a and m_b cannot be multiplied.
    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """

    if m_a == [] or m_a == [[]]:
        # Raise a ValueError if m_a is empty or contains only an empty list
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        # Raise a ValueError if m_b is empty or contains only an empty list
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        # Raise a TypeError if m_a is not a list
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        # Raise a TypeError if m_b is not a list
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        # Raise a TypeError if m_a contains elements that are not lists
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        # Raise a TypeError if m_b contains elements that are not lists
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_a for num in row]):
        # Raise a TypeError if m_a contains elements that are not integers or floats
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_b for num in row]):
        # Raise a TypeError if m_b contains elements that are not integers or floats
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        # Raise a TypeError if rows in m_a have different sizes
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        # Raise a TypeError if rows in m_b have different sizes
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        # Raise a ValueError if the number of columns in m_a is not equal to the number of rows in m_b
        raise ValueError("m_a and m_b can't be multiplied")


    inverted_b = []
    for r in range(len(m_b[0])):
        new_row = []
        for c in range(len(m_b)):
            new_row.append(m_b[c][r])
        inverted_b.append(new_row)

    new_matrix = []
    for row in m_a:
        new_row = []
        for col in inverted_b:
            prod = 0
            for i in range(len(inverted_b[0])):
                prod += row[i] * col[i]
            new_row.append(prod)
        new_matrix.append(new_row)

    return new_matrix
