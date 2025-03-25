import os
import time
import humanize

def get_file_metadata(file_path):
    """Extracts metadata for a given file and returns it as a dictionary."""
    if not os.path.exists(file_path):
        return None

    metadata = {
        "File Name": os.path.basename(file_path),
        "Size": humanize.naturalsize(os.path.getsize(file_path)),
        "Created": time.ctime(os.path.getctime(file_path)),
        "Last Modified": time.ctime(os.path.getmtime(file_path)),
        "Last Accessed": time.ctime(os.path.getatime(file_path)),
        "File Type": os.path.splitext(file_path)[1] or "Unknown",
    }

    return metadata  # Returning metadata instead of printing
