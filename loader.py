import os
import json
import yaml


ALLOWED_EXTENSIONS = ["json", "yaml", "txt", "csv"]


def get_valid_files(folder: str):
    # Get the valid files in the folder.
    files = [os.path.abspath(os.path.join(folder, f)) for f in os.listdir(folder) if not f.startswith(".")]
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
    return obj


def load_txt(fn: str, data: dict):
    try:
        with open(fn, "r") as f:
            obj = f.readlines()
    except Exception as e:
        raise e
    for line in obj:
        new_note = {}
        l = line.split(",")
        if l[0] == "simple_translate":
            new_note["sentence"] = l[1]
            new_note["translation"] = l[2]
            data["simple_translate"].append(new_note)
        elif l[0] == "to_fill":
            new_note["sentence"] = l[1]
            new_note["explanation"] = l[2]
            new_note["words_to_fill"] = l[3:]
            data["to_fill"].append(new_note)
        else:
            continue
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
    return data
