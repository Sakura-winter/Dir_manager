import sys
import os

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QFileDialog,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QLabel, QComboBox, QMessageBox
)
from PyQt6.QtWidgets import QInputDialog
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import humanize  # For better file size formatting
import subprocess  # For opening files
from PyQt6.QtWidgets import QLineEdit  # Import for search bar

class DirectoryManager(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("AI-Powered Directory Manager")
        self.setGeometry(100, 100, 800, 600)

        # Create central widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.setup_search_bar()  # Add search bar

        # Label to display selected directory
        self.dir_label = QLabel("No directory selected", self)
        self.dir_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.dir_label)

        # Button to browse and select directory
        self.browse_button = QPushButton("Browse Directory")
        self.browse_button.clicked.connect(self.browse_directory)
        self.layout.addWidget(self.browse_button)

        # Sorting dropdown
        self.sort_by_dropdown = QComboBox()
        self.sort_by_dropdown.addItems(["Name", "Size", "Type", "Last Modified"])
        self.sort_by_dropdown.currentIndexChanged.connect(self.sort_files)
        self.layout.addWidget(self.sort_by_dropdown)

        # Table to display file details
        self.file_table = QTableWidget()
        self.file_table.setColumnCount(4)
        self.file_table.setHorizontalHeaderLabels(["File Name", "Size", "Type", "Last Modified"])
        self.file_table.setSortingEnabled(True)  # Enable sorting
        self.layout.addWidget(self.file_table)

        # Buttons for file operations
        self.open_button = QPushButton("Open File")
        self.open_button.clicked.connect(self.open_file)
        self.layout.addWidget(self.open_button)

        self.rename_button = QPushButton("Rename File")
        self.rename_button.clicked.connect(self.rename_file)
        self.layout.addWidget(self.rename_button)

        self.delete_button = QPushButton("Delete File")
        self.delete_button.clicked.connect(self.delete_file)
        self.layout.addWidget(self.delete_button)

        # Storage for file details
        self.files_data = []  # Holds the file info for sorting

    def browse_directory(self):
        """Opens a dialog to select a directory and lists its files."""
        folder_path = QFileDialog.getExistingDirectory(self, "Select Directory")
        if folder_path:
            self.dir_label.setText(f"Selected Directory: {folder_path}")
            self.list_files(folder_path)

    #from PyQt6.QtWidgets import QLineEdit  # Import for search bar

    def setup_search_bar(self):
        """Creates a search bar to filter files dynamically."""
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Search files...")
        self.search_bar.textChanged.connect(self.filter_files)
        self.layout.insertWidget(1, self.search_bar)  # Insert above table

    def filter_files(self):
        """Filters table rows based on search query."""
        query = self.search_bar.text().lower()

        for row in range(self.file_table.rowCount()):
            file_name = self.file_table.item(row, 0).text().lower()
            file_ext = self.file_table.item(row, 2).text().lower()

            if query in file_name or query in file_ext:
                self.file_table.setRowHidden(row, False)
            else:
                self.file_table.setRowHidden(row, True)

    def list_files(self, folder_path):
        """Lists all files in the selected directory and displays them in the table."""
        self.files_data.clear()  # Clear previous data
        self.file_table.setRowCount(0)  # Clear table

        files = os.listdir(folder_path)

        for file_name in files:
            file_path = os.path.join(folder_path, file_name)

            if os.path.isfile(file_path):  # Only list files, not directories
                try:
                    file_size = os.path.getsize(file_path)
                    formatted_size = humanize.naturalsize(file_size)
                    file_ext = os.path.splitext(file_name)[1] or "Unknown"
                    last_modified = os.path.getmtime(file_path)
                    formatted_modified = humanize.naturaltime(last_modified)

                    # Store data for sorting
                    self.files_data.append((file_name, file_size, file_ext, last_modified))

                except Exception as e:
                    print(f"Error processing {file_name}: {e}")  # Print errors in terminal

        self.populate_table()

    def populate_table(self):
        """Populates the table with sorted file data."""
        self.file_table.setRowCount(0)

        for file_name, file_size, file_ext, last_modified in self.files_data:
            formatted_size = humanize.naturalsize(file_size)
            formatted_modified = humanize.naturaltime(last_modified)

            row_position = self.file_table.rowCount()
            self.file_table.insertRow(row_position)
            self.file_table.setItem(row_position, 0, QTableWidgetItem(file_name))
            self.file_table.setItem(row_position, 1, QTableWidgetItem(formatted_size))
            self.file_table.setItem(row_position, 2, QTableWidgetItem(file_ext))
            self.file_table.setItem(row_position, 3, QTableWidgetItem(formatted_modified))

    def sort_files(self):
        """Sorts the files based on the selected sorting method."""
        sort_option = self.sort_by_dropdown.currentText()

        if sort_option == "Name":
            self.files_data.sort(key=lambda x: x[0].lower())  # Sort by file name
        elif sort_option == "Size":
            self.files_data.sort(key=lambda x: x[1])  # Sort by file size
        elif sort_option == "Type":
            self.files_data.sort(key=lambda x: x[2].lower())  # Sort by file type
        elif sort_option == "Last Modified":
            self.files_data.sort(key=lambda x: x[3], reverse=True)  # Sort by last modified time (latest first)

        self.populate_table()  # Update the table after sorting



    def open_file(self):
        selected_row = self.file_table.currentRow()
        if selected_row == -1:
            return  # No selection

        file_name = self.file_table.item(selected_row, 0).text()
        folder_path = self.dir_label.text().replace("Selected Directory: ", "").strip()
        file_path = os.path.join(folder_path, file_name)

        if os.path.exists(file_path):
            try:
                os.startfile(file_path)  # Windows
            except Exception as e:
                print(f"Error opening file: {e}")



    def rename_file(self):
        selected_row = self.file_table.currentRow()
        if selected_row == -1:
            return

        file_name = self.file_table.item(selected_row, 0).text()
        folder_path = self.dir_label.text().replace("Selected Directory: ", "").strip()
        file_path = os.path.join(folder_path, file_name)

        new_name, ok = QInputDialog.getText(self, "Rename File", "Enter new name:")
        if ok and new_name:
            new_path = os.path.join(folder_path, new_name)
            try:
                os.rename(file_path, new_path)
                self.list_files(folder_path)  # Refresh table
            except Exception as e:
                print(f"Error renaming file: {e}")



    def delete_file(self):
        selected_row = self.file_table.currentRow()
        if selected_row == -1:
            return

        file_name = self.file_table.item(selected_row, 0).text()
        folder_path = self.dir_label.text().replace("Selected Directory: ", "").strip()
        file_path = os.path.join(folder_path, file_name)

        reply = QMessageBox.question(self, "Confirm Delete", f"Are you sure you want to delete '{file_name}'?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            try:
                os.remove(file_path)
                self.list_files(folder_path)  # Refresh table
            except Exception as e:
                print(f"Error deleting file: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DirectoryManager()
    window.show()
    sys.exit(app.exec())
