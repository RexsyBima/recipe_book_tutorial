import json
from json.decoder import JSONDecodeError


def save_json(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f)


def update_json(usernames, user, filename):
    for u in usernames:
        if u == user["username"]:
            usernames[u]["recipes"] = user["recipes"]
        save_json(usernames, filename)


def read_json(filename):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            return data
    except JSONDecodeError:
        return {}


def print_enumerate(data: list[dict[str : str | list]], key: str, title: str):
    print(title)
    for index, item in enumerate(data, start=1):
        print(f"{index}. {item[key]}")
