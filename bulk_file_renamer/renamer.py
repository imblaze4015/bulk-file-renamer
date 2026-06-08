# Goal: Function that takes a folder path and renames all files sequentailly.

from pathlib import Path

def bulk_rename(folder_path: str, dry_run: bool = True) -> None:
    # Rename all files in folder_path (dry run first).
    # If dry_run is True, only print planned renames.
    # If dry_run is False, actually rename files
    
    folder = Path(folder_path)
    print(f"Looking in folder: {folder}")
    
    counter = 1 # number for new file name
    
    # Collect all files in the folder (ignore sub-folders)
    for item in folder.iterdir():
        if item.is_file():
            
            extension = item.suffix # e.g., .jpg, .txt, etc
            new_name = f"file_{counter}{extension}"
            new_path = folder / new_name # full path of the new name
            
            if dry_run:
                print(f"Would rename: {item.name} -> {new_name}")
            else:
                item.rename(new_path)
                print(f"Renamed: {item.name} -> {new_name}")
                
            counter += 1
            
            
