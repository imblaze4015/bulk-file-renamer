# Goal: Function that takes a folder path and renames all files sequentailly.

from pathlib import Path

def bulk_rename(folder_path: str) -> None:
    # Given a folder, list all files (not directories) inside it, print each file name found
    
    folder = Path(folder_path)
    
    print(f"Looking in folder: {folder}")
    
    # Collect all files in the folder (ignore sub-folders)
    for item in folder.iterdir():
        if item.is_file():
            print(f"Found file: {item.name}")
            
