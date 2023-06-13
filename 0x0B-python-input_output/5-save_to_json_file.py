#!/usr/bin/python3
'''
Function to write a Python object to a text file using JSON representation.
'''

import json

def save_to_json_file(my_obj, filename):
'''
Writes a Python object to a text file using JSON representation
Args:
    my_obj (any): The Python object to be serialized and written to the file.
    filename (str): The name of the file to write the JSON representation to.
'''
with open(filename, 'w') as f:
    f.write(json.dumps(my_obj))
