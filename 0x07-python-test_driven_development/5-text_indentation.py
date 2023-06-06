#!/usr/bin/python3
"""Defines a function for printing indented text."""


def text_indentation(text):
    """Prints a text with indentation.

    Args:
        text (str): The text to be printed.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ['.', '?', ':']
    lines = text.splitlines()

    for line in lines:
        line = line.strip()  # Remove leading/trailing spaces

        if line == "":
            continue  # Skip empty lines

        for separator in separators:
            if separator in line:
                line = line.replace(separator, f"{separator}\n\n")

        print(line)

