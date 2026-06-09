from src.bulk_file_renamer.renamer import bulk_rename

# Temporary: always dry-run on the test_files folder
if __name__ == "__main__":
    print("Running renamer on 'test_files' folder...")
    bulk_rename("test_files", dry_run=True)