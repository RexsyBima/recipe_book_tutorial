import json
from json.decoder import JSONDecodeError


def save_json(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f)


def read_json(filename):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            return data
    except JSONDecodeError:
        return {}
