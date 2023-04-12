#!/usr/bin/python3
"""Module defines a JSON function for file writing"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
