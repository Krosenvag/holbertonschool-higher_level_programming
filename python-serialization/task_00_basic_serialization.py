#!/usr/bin/python3
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Parameters:
    data (dict): The Python dictionary serialize.
    filename (str): The filename output JSON file  the file exists, replaced.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)
    print(f"Data serialized and saved to '{filename}'.")


def load_and_deserialize(filename):
    """
    Load and deserialize a JSON file to a Python dictionary.

    Parameters:
    filename (str): The filename of the input JSON file.

    Returns:
    dict: The deserialized Python dictionary.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
