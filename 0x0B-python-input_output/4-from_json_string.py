#!/usr/bin/python3
'''
Function to convert a JSON string to a Python object (data structure).
'''

import json

def from_json_string(my_str):
'''
Converts a JSON string to a Python object.
Args:
    my_str (str): The JSON string to be deserialized.

Returns:
    any: The Python object represented by the JSON string.
'''
return (json.loads(my_str))
