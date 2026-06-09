from pathlib import Path

def bulk_rename(folder_path: str, dry_run: bool = True) -> None:
    """
    Rename all files in folder_path sequentially.
    Files are sorted alphabetically before renaming.
    """
    folder = Path(folder_path)
    print(f"Looking in folder: {folder}")

    # Collect and sort files by name for a predictable order
    files = sorted(
        [item for item in folder.iterdir() if item.is_file()],
        key=lambda f: f.name
    )

    counter = 1

    for item in files:
        extension = item.suffix
        new_name = f"file_{counter}{extension}"
        new_path = folder / new_name

        if dry_run:
            print(f"Would rename: {item.name}  ->  {new_name}")
        else:
            item.rename(new_path)
            print(f"Renamed: {item.name}  ->  {new_name}")

        counter += 1