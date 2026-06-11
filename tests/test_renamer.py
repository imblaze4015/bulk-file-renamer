import os
import tempfile
from pathlib import Path
from bulk_file_renamer.renamer import bulk_rename


def test_dry_run_does_not_crash():
    """Smoke test: dry run on test_files folder does not crash."""
    print("Running test: dry-run on test_files/")
    bulk_rename("test_files", dry_run=True)
    print("Test passed: no crash!")


def test_renaming_works_correctly():
    """Create dummy files, rename them, and check the result."""
    # SETUP: create a temporary folder that cleans itself up
    with tempfile.TemporaryDirectory() as tmpdir:
        folder = Path(tmpdir)

        # Create three files with unsorted names (like a real folder)
        (folder / "zebra.txt").write_text("zebra content")
        (folder / "apple.csv").write_text("apple content")
        (folder / "mango.jpg").write_text("mango content")

        # ACTION: run the renamer (real run, not dry)
        bulk_rename(str(folder), dry_run=False)

        # ASSERTION: collect the remaining file names, sorted
        remaining = sorted(f.name for f in folder.iterdir() if f.is_file())

        # Check we have exactly the expected files in the expected order
        expected = ["file_1.csv", "file_2.jpg", "file_3.txt"]
        assert remaining == expected, f"Expected {expected}, got {remaining}"

        # Check that the old names really disappeared
        assert not (folder / "zebra.txt").exists()
        assert not (folder / "apple.csv").exists()
        assert not (folder / "mango.jpg").exists()

        print("Test passed: renaming worked correctly.")