import json # Import json to enable usage of the .json format

# Read the json file given by path, return it
def read(path: str):
    with open(path, "r") as f:
        data = json.load(f)
    return data

# Add a dict to the list in the json file given by path
def append_to_json(path: str, to_append: dict):
    # Save the current contents of path
    with open(path, "r") as f:
        data = json.load(f) 
    
    # Overwrite path with the current contents + the dict to append
    data.append(to_append)
    with open(path, "w") as f:
        json.dump(data, f)