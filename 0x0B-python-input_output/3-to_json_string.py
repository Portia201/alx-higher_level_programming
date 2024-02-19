#!/usr/bin/python3
"""Defines a string-to-JSON function."""

import json

def to_json_string(my_obj):
    """Return the JSON representation string of a objet."""
    return json.dumps(my_obj)
