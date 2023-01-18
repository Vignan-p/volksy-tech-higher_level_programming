#!/usr/bin/python3
"""json"""
import sys
save_to_json_file = __import__(5-save_to_json_file.py).save_to_json_file
load_from_json_file = __import__(6-load_from_json_file.py).load_from_json_file

try:
    load_file = load_from_json_file("add_item.json")
except:
    load_file = []

arg = len(sys.argv)
for i in range(1, arg):
    load_file.append(sys.argv[i])

save_to_json_file(load_file, "add_item.json")

