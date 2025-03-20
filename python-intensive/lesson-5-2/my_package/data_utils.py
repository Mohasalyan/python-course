import json

def dict_to_json(data: dict) -> str:
    """
    Converts a dictionary to a JSON string.
    """
    return json.dumps(data, indent=4)


def json_to_dict(json_str: str) -> dict:
    """
    Converts a JSON string to a dictionary.
    """
    return json.loads(json_str)
