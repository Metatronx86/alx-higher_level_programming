#!/usr/bin/python3
'''
Function to convert an object to its JSON representation (string).
'''

import json

def to_json_string(my_obj):
'''
Converts an object to its JSON representation
Args:
    my_obj (any): The object to be serialized to JSON.

Returns:
    str: The JSON representation of the object.
'''
return (json.dumps(my_obj))
