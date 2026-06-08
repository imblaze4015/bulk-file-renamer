# Bulk File Renamer

A Python tool to rename all files in a folder sequentially.

## Installation

1. **Clone the repository:**  
   ```bash
   git clone https://github.com/your-imblaze4015/bulk-file-renamer.git
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Linux/macOS
   python3 -m venv .venv
   source .venv/bin/activate

   # Windows
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install the project and test dependencies:**
   ```bash
   pip install -e ".[test]"
   ```

4. **Run the tests to confirm everything works:**
   ```bash
   pytest
   ```

## Usage

In a Python script or interactive session:

```python
from bulk_file_renamer.renamer import bulk_rename

# Dry run (safe) - prints planned rename without changing files
bulk_rename("path/to/your/folder", dry_run=True)

# Real run - actually rename files
bulk_rename("path/to/your/folder", dry_run=False)
```
