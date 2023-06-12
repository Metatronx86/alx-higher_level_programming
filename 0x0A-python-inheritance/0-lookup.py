#!/usr/bin/python3

def lookup(obj):
  """Returns a list of the available attributes and methods of an object.

  Args:
    obj: The object to lookup.

  Returns:
    A list of strings, where each string is the name of an attribute or method of the object.
  """

  attributes = []
  methods = []
  for attr in dir(obj):
    if not callable(getattr(obj, attr)):
      attributes.append(attr)
    else:
      methods.append(attr)

  return attributes + methods

