import os
import shutil

import json

def load_file_types(path="file_types.json"):

    try:
        with open(path,"r") as f:
            file_types = json.load(f)
    except FileNotFoundError:
        print("file_types.json not found.")
        file_types = {}

    return file_types

def save_file_types(data_types,path="file_types.json"):
    with open(path,"w") as f:
        json.dump(f,data_types)

def organize_files(folder):
    changes = []
    file_types = load_file_types()
    files = os.listdir(folder)
    other_files = files.copy()

    for file in files:
        path = os.path.join(folder, file)

        if os.path.isdir(path):
            if file in other_files:
                other_files.remove(file)
            continue

        _, extension = os.path.splitext(file)

        for key, exe in file_types.items():
            if extension.lower() in exe:
                changes.append(move_file(path, key))
                if file in other_files:
                    other_files.remove(file)
                break

    for other in other_files:
        changes.append(move_file(os.path.join(folder, other), "Others"))

    return changes


def move_file(path,key):
    root,name = os.path.split(path)
    directory = os.path.join(root,key)
    os.makedirs(directory,exist_ok=True)
    direct,file_name = os.path.split(path)
    try:
        shutil.move(path,directory)
        return f"{file_name} Moved to {directory}"
    except shutil.Error:
        return f"{file_name} already exist"

