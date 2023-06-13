#!/usr/bin/python3
"""
Python script to add all arguments to a Python list.
The list is then saved to a file using JSON representation.
"""

import sys
from typing import List
from json import load_from_json_file, save_to_json_file

def add_args_to_list(args: List[str]) -> List[str]:
"""
Adds all arguments to a Python list.
Args:
    args (List[str]): The command-line arguments to be added to the list.

Returns:
    List[str]: The updated list containing all the arguments.
"""
my_list = load_from_json_file("add_item.json") if args else []
my_list.extend(args)
return my_list
if name == "main":
arguments = sys.argv[1:] # Exclude the script name from the arguments
updated_list = add_args_to_list(arguments)
save_to_json_file(updated_list, "add_item.json")





