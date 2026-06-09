# Bulk File Renamer

A Python tool to rename all files in a folder sequentially.

## Installation

1. **Clone the repository:**  
   ```bash
   git clone git clone https://github.com/imblaze4015/bulk-file-renamer.git
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

### Command line (recommended)

```bash
# Safe dry run — prints what would happen without renaming
python -m bulk_file_renamer path/to/your/folder

# Real rename — actually renames files
python -m bulk_file_renamer path/to/your/folder --execute
```

### From Python code

```python
from bulk_file_renamer.renamer import bulk_rename

bulk_rename("path/to/your/folder", dry_run=True)   # safe preview
bulk_rename("path/to/your/folder", dry_run=False)  # real renamea
```
