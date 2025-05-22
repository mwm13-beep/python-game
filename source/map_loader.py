# map_loader.py
import json
from grid import Grid

def from_array(array2d):
    return Grid.from_array(array2d)

def from_json_file(path):
    with open(path, "r") as f:
        data = json.load(f)
    return Grid.from_array(data)

# placeholder for future loading methods
def from_tmx_file(path):
    raise NotImplementedError("TMX support not implemented yet.")
