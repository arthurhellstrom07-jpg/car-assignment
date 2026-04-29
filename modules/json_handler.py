import json

def read(path: str):
    with open(path, "r") as f:
        data = json.load(f)
    return data

def append_to_json(path: str, to_append: dict):
    with open(path, "r") as f:
        data = json.load(f) 
    
    data.append(to_append)
    with open(path, "w") as f:
        json.dump(data, f)