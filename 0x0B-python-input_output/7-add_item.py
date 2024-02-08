#!/usr/bin/python3
import sys
from os.path import exists
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

# Name of the JSON file
json_file = 'add_item.json'

# Check if the JSON file already exists
if exists(json_file):
    # Load existing items from the JSON file
    items = load_from_json_file(json_file)
else:
    # Create an empty list if the JSON file doesn't exist
    items = []

# Append all arguments to the list
for arg in sys.argv[1:]:
    items.append(arg)

# Save the updated list to the JSON file
save_to_json_file(items, json_file)

