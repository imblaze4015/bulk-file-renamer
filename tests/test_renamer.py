from bulk_file_renamer.renamer import bulk_rename

def test_dry_run_does_not_crash():
    """
    Run bulk_rename in dry_run mode on test_files folder and print success.
    """
    print("Running test: dry-run on test_files/")
    bulk_rename("test_files", dry_run=True)
    print("Test passed: no crash!")