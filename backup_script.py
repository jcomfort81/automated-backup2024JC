import os
import shutil
from datetime import datetime

def backup_directory(source_dir, backup_dir):
    # Ensure the source directory exists
    if not os.path.exists(source_dir):
        print(f"Source directory {source_dir} does not exist.")
        return

    # Create a timestamped backup directory
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = os.path.join(backup_dir, f"backup_{timestamp}")

    try:
        shutil.copytree(source_dir, backup_path)
        print(f"Backup of {source_dir} completed successfully at {backup_path}")
    except Exception as e:
        print(f"Error during backup: {e}")

if __name__ == "__main__":
    source_directory = "/path/to/source_directory"
    backup_directory = "/path/to/backup_directory"
    backup_directory(source_directory, backup_directory)
