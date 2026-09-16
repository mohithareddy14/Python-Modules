"""Demonstrates json.dumps() for converting Python data into a JSON string."""

import json


def convert_to_json():
    """Convert a Python dictionary into a JSON string."""

    data = {
        "name": "Geetha",
        "role": "Data Analyst",
        "skills": ["Python", "SQL", "Excel"]
    }

    return json.dumps(data)