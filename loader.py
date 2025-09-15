""" loader module

The goal is to accept the most useful sources format that user may need.
It must be done by allowing easy integration of new note types in the future.

So the process should be the following:

    - Check the source(s) file(s) are valid.
    - Load from the specific source and rapid transform the data so it's a list
      of dicts with key = field, value = its value.
    - This dict is then pass to the same 'factory' method so it builds the corresponding
      object.

current schema :

``` json
    [
        {
            "type": "",
            "sentence": "",
            "translation": "",
            "explanation": "",
            "words_to_hide": ["",""],
        },
        ...
    ]
```

"""
import os
import csv
import json
import yaml
from collections import defaultdict


ALLOWED_EXTENSIONS = ["json", "yaml", "txt", "csv"]


def get_valid_files(folder: str):
    """ Get the files from the data directory that have an allowed extension
    and do not start by a ".".

    Args:

        folder (str): folder or file from which the data is loaded.
    """
    if os.path.isfile(folder):
        files = [folder]
    elif os.path.isdir(folder):
        files = [os.path.abspath(os.path.join(folder, f)) for f in os.listdir(folder) if not f.startswith(".")]
    else:
        raise Exception("Error: the folder/file doesn't exist.")
    valid_files = {}
    for ext in ALLOWED_EXTENSIONS:
        valid_files[ext] = []
    for f in files:
        parsed_fn = f.split(".")
        if len(f.split(".")) != 2:
            continue
        if not parsed_fn[1] in ALLOWED_EXTENSIONS:
            continue
        valid_files[parsed_fn[1]].append(f)
    return valid_files


def make_new_note(obj: dict, data: dict):
    """ Turns a list into its valid custom anki object.

    Args
        obj (dict): the dict representation of a anki note.
        data (dict): the current loaded data.
    """
    new_note = {}
    if obj["type"] == "simple_translate":
        new_note["sentence"] = obj["sentence"]
        new_note["translation"] = obj["translation"]
        data["simple_translate"].append(new_note)
    elif obj["type"] == "to_fill":
        new_note["sentence"] = obj["sentence"]
        new_note["explanation"] = obj["explanation"]
        new_note["words_to_hide"] = obj["words_to_hide"]
        data["to_fill"].append(new_note)
    return data


def load_json(fn: str, data: dict):
    """ Load the data from json file. """
    try:
        with open(fn, "r") as f:
            objs = json.load(f)
    except json.JSONDecodeError as e:
        raise e
    if not isinstance(obj, list):
        raise Exception("Json object should be a list.")
    for obj in objs:
        data = make_new_note(obj, data)
    return data


def load_yaml(fn: str, data: dict):
    try:
        with open(fn, "r") as f:
            objs = yaml.safe_load(f)
    except yaml.YAMLError as e:
        raise e
    if not isinstance(obj, dict):
        raise Exception(f"{fn} is not a valid yaml file.")
    for obj in objs:
        data = make_new_note(obj, data)
    return data


def load_csv(fn: str, data: dict):
    try:
        csv_data = []
        with open(fn, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["words_to_hide"] = row["words_to_hide"].split(";")
                csv_data.append(row)
    except Exception as e:
        raise e
    for obj in csv_data:
        make_new_note(obj, data)


def load_notes(folder: str):
    # Load the data in memory
    valid_files = get_valid_files(folder)
    # This 'data' dict is edited on the fly so it's thread unsafe.
    data = {
        "simple_translate": [],
        "to_fill": []
    }
    for f in valid_files["json"]:
        load_json(f, data)
    for f in valid_files["csv"]:
        load_csv(f, data)
return data
