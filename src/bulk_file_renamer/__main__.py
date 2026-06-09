from src.bulk_file_renamer.renamer import bulk_rename
import sys

# Temporary: always dry-run on the test_files folder
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a folder path.")
        print("Example: python -m bulk_file_renamer test_files")
        exit(1)

    folder = sys.argv[1]

    # Check if the user added the --execute flag
    do_dry_run = True
    if "--execute" in sys.argv:
        do_dry_run = False

    print(f"Running renamer on: {folder}")
    bulk_rename(folder, dry_run=do_dry_run)