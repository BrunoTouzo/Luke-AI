import json
import os

# reading info inside a json file
def load_json(path:str)->dict | None:
    try:
        with open(os.path.abspath(path.strip()), "r") as file:
            dump:dict = json.load(file)
            return dump

    except Exception as e:
        print(e)
        return None

# saving info inside a json file
def save_json(path:str, data:dict)->int:
    try:
        with open(os.path.abspath(path.strip()), "w", encoding="latin-1") as file:
            json.dump(data, file, indent=4)
            return 1

    except Exception as e:
        print(e)
        return -1
