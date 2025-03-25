import os
import time
import humanize
from tkinter import *
from tkinter import ttk

def get_file_metadata(file_path):
    """Extracts metadata for a given file."""
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

    return metadata

# Function to display metadata
def display_metadata(file_path):
    metadata = get_file_metadata(file_path)
    if metadata:
        metadata_text.delete(1.0, END)  # Clear previous text
        for key, value in metadata.items():
            metadata_text.insert(END, f"{key}: {value}\n")

# GUI setup
root = Tk()
root.title("Metadata Viewer")
root.geometry("600x400")

# File Selection Button
def select_file():
    from tkinter import filedialog
    file_path = filedialog.askopenfilename()
    if file_path:
        display_metadata(file_path)

btn_select = Button(root, text="Select File", command=select_file)
btn_select.pack(pady=10)

# Metadata Display Area
metadata_text = Text(root, height=10, width=70)
metadata_text.pack(padx=10, pady=10)

root.mainloop()

