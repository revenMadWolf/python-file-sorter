import os
import shutil

file_types = {"Images": [".jpg", ".jpeg", ".png", ".gif",".webp",".avif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv",".mpeg",".ogg"],
    "Audio" : [".mp3",".wav"],
    "Archives":[".zip",".rar",".7z"],
    "Others": []}

def organize_files(folder):
    changes = []
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
