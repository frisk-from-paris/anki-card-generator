import os
import csv
import json
import yaml


ALLOWED_EXTENSIONS = ["json", "yaml", "txt", "csv"]


def get_valid_files(folder: str):
    """ Get the files from the data directory that have an allowed extension
    and do not start by a ".".
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


def make_new_note(obj: list, data: dict):
    """ Turns a list into its valid anki object. """
    new_note = {}
    if obj[0] == "simple_translate":
        new_note["sentence"] = obj[1]
        new_note["translation"] = obj[2]
        data["simple_translate"].append(new_note)
    elif obj[0] == "to_fill":
        new_note["sentence"] = obj[1]
        new_note["explanation"] = obj[2]
        new_note["words_to_fill"] = obj[3:]
        data["to_fill"].append(new_note)
    return data


def load_json(fn: str, data: dict):
    """ Load the data from json file.
    We expect a json as following:

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
    try:
        obj = json.load(fn)
    except json.JSONDecodeError as e:
        raise e
    if not isinstance(obj, list):
        raise Exception("Json object should be a list.")
    return obj


def load_yaml(fn: str, data: dict):
    try:
        obj = yaml.safe_load(fn)
    except yaml.YAMLError as e:
        raise e
    if not isinstance(obj, dict):
        raise Exception(f"{fn} is not a valid yaml file.")


def load_txt(fn: str, data: dict):
    try:
        with open(fn, "r") as f:
            obj = f.readlines()
    except Exception as e:
        raise e
    for line in obj:
        new_note = {}
        l = line.split(",")
        data = make_new_note(l, data)
    return data


def load_csv(fn: str, data: dict):
    try:
        with open(fn, "r") as f:
            reader = csv.reader(f, delimiter=",")
            csv_data = list(reader)
    except Exception as e:
        raise e

    keys = csv_data.pop(0)
    for line in csv_data:
        formatted = []
        formatted.append(line[0])
        if line[0] == "simple_translate":
            formatted.append(line[1])
            formatted.append(line[2])
        elif line[0] == "to_fill":
            formatted.append(line[1])
            formatted.append(line[3])
            formatted.extend(line[4:])
        data = make_new_note(formatted, data)
    return data


def load_notes(folder: str):
    # Load the data in memory
    valid_files = get_valid_files(folder)
    data = {
        "simple_translate": [],
        "to_fill": []
    }
    for f in valid_files["json"]:
        data = load_json(f, data)
    for f in valid_files["txt"]:
        data = load_txt(f, data)
    for f in valid_files["csv"]:
        data = load_csv(f, data)
    return data
