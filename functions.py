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
        json.dump(data_types,f)

def organize_files(folder,is_other_active,is_rename_active):
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
                changes.append(move_file(path, key,is_rename_active))
                if file in other_files:
                    other_files.remove(file)
                break
    if is_other_active:
        for other in other_files:
            changes.append(move_file(os.path.join(folder, other), "Others",is_rename_active))

    return changes


def move_file(path, key, is_rename_active):
    root, name = os.path.split(path)
    directory = os.path.join(root, key)
    os.makedirs(directory, exist_ok=True)

    destination = os.path.join(directory, name)

    if not os.path.exists(destination):
        shutil.move(path, destination)
        return f"{name} Moved to {directory}"

    elif not is_rename_active:
        return f"{name} already exists"

    else:
        count = 1
        base, ext = os.path.splitext(name)

        while True:
            new_name = f"{base}({count}){ext}"
            new_destination = os.path.join(directory, new_name)

            if not os.path.exists(new_destination):
                shutil.move(path, new_destination)
                return f"{name} renamed to {new_name} and moved to {directory}"

            count += 1






