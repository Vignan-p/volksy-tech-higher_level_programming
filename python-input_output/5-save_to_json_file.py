#!/usr/bin/python3
"""JSON"""
import json


def save_to_json_file(my_obj, filename):
    """JSON write"""
    with open(filename, mode='w', encoding="utf-8") as f:
        return (f.write(json.dumps(my_obj)))
