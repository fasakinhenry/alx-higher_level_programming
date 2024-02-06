#!/usr/bin/python3
"""This script adds all the arguments to a python list.
Then save the list to a file.
"""
import sys
save_to_json = __import__("5-save_to_json_file").save_to_json_file
load_from_json = __import__("6-load_from_json_file").load_from_json_file
command_line_args = sys.argv[1:]

try:
    args = load_from_json("add_item.json")
    for i in command_line_args:
        args.append(i)
    save_to_json(args, "add_item.json")
except FileNotFoundError:
    save_to_json(command_line_args, "add_item.json")
