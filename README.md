Got it 👍 — here’s a **general-purpose README** that works for backing up *any file or folder*, not just Minecraft:

```markdown
# File Backup Script

This script automatically creates a dated backup of a file.  
It is useful for keeping safe copies of documents, projects, saves, or any other files you don’t want to lose.

## How It Works
- Looks for a source file at the path you specify (example in the script).
- Moves (not copies) the file into your chosen backup folder.
- The backup file is renamed to include the current date, e.g.:
```

2025-08-17\_backup.ext

````

## Requirements
- Python 3.x installed
- Standard library only (no external dependencies)

## Usage
1. Open the script in a text editor.
2. Set your file path:
 ```python
 src = r'C:\path\to\your\file.txt'
````

3. Set your backup folder:

   ```python
   dst = fr'D:\backups\{today}_backup.txt'
   ```
4. Run the script:

   ```sh
   python backup.py
   ```
5. If the source file exists, it will be moved to the backup folder.
   If it does not exist, you’ll see:

   ```
   Source file does not exist.
   ```

## Notes

* The script uses `shutil.move`, which removes the original after creating the backup.
* If you want to **keep the original** and just make a copy, replace:

  ```python
  shutil.move(src, dst)
  ```

  with:

  ```python
  shutil.copy(src, dst)
  ```

---

✅ Useful for keeping safe versions of any file (documents, code, saves, etc.) with a simple timestamped backup system.

```
