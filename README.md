# 📂 AI-Powered Directory Management System

An **intelligent and efficient directory management system** that utilizes AI for file categorization, duplicate detection, and metadata extraction. Designed to enhance **file organization, searchability, and management**, this tool provides a seamless user experience with advanced automation features.

![Python](https://img.shields.io/badge/Python-3.13-blue.svg)  
![PyQt6](https://img.shields.io/badge/UI-PyQt6-red)  
![PyInstaller](https://img.shields.io/badge/Built%20With-PyInstaller-orange)  
![OpenCV](https://img.shields.io/badge/Image%20Processing-OpenCV-blue)  
![Tesseract OCR](https://img.shields.io/badge/OCR-Tesseract-green)  
![pandas](https://img.shields.io/badge/Data%20Handling-pandas-lightblue)  
![NumPy](https://img.shields.io/badge/Numerical%20Computing-NumPy-yellow)  
![hashlib](https://img.shields.io/badge/File%20Hashing-hashlib-purple)  
![MIT License](https://img.shields.io/badge/License-MIT-green)  

---
## 📌 Dependencies  

Below are the key dependencies used in this project:  

| **Dependency** | **Purpose** |  
|--------------|------------|  
| `PyQt6` ![PyQt6](https://img.shields.io/badge/UI-PyQt6-red) | Graphical User Interface (GUI) |  
| `PyInstaller` ![PyInstaller](https://img.shields.io/badge/Built%20With-PyInstaller-orange) | Converts Python script into a standalone executable |  
| `OpenCV` ![OpenCV](https://img.shields.io/badge/Image%20Processing-OpenCV-blue) | Image processing & metadata extraction |  
| `Tesseract OCR` ![Tesseract OCR](https://img.shields.io/badge/OCR-Tesseract-green) | Optical Character Recognition (OCR) for extracting text from images |  
| `pandas` ![pandas](https://img.shields.io/badge/Data%20Handling-pandas-lightblue) | Data manipulation for file details |  
| `NumPy` ![NumPy](https://img.shields.io/badge/Numerical%20Computing-NumPy-yellow) | Numerical operations |  
| `hashlib` ![hashlib](https://img.shields.io/badge/File%20Hashing-hashlib-purple) | Used for detecting duplicate files |  

---

## 🚀 Features  

✅ **AI-Powered File Categorization** – Automatically classifies files into categories based on their content.  
✅ **File Preview** – Allows users to preview text files, images, and PDFs before opening them.  
✅ **Metadata Extraction** – Extracts key metadata (file size, creation date, format, etc.).  
✅ **User-Friendly Interface** – Simple and intuitive UI for easy navigation.  
✅ **Fast & Efficient** – Optimized performance for handling large directories.  

---

## 🛠 Installation & Setup  

### 🔹 **Prerequisites**  
Ensure you have **Python 3.13** installed.  

### 🔹 **Step 1: Clone the Repository**  
```sh
git clone https://github.com/Sakura-winter/Dir_manager.git
cd Dir_manager
```

### 🔹 **Step 2: Create a Virtual Environment**  
```sh
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux
.venv\Scripts\activate    # On Windows
```
### 🔹 **Step 3: Install Dependencies**  
Run the following command to install all required dependencies:  

```sh
pip install -r requirements.txt
```
## 📌 Module Breakdown  

The **AI-Powered Directory Management System** is divided into three key modules to ensure a structured and efficient workflow.

---

### **🔹 Module 1: User Interface & Interaction (PyQt6)**  
📌 **Purpose:**  
This module is responsible for the **graphical user interface (GUI)**, allowing users to interact with the system easily. It enables directory selection, file browsing, sorting, and filtering.  

📌 **Key Components:**  
✅ **Graphical User Interface (GUI)** – Developed using PyQt6.  
✅ **Directory Selection** – Allows users to browse and select directories.  
✅ **File Table Display** – Lists all files in a structured format.  
✅ **Sorting & Filtering** – Provides multiple sorting options for better organization.  
✅ **Category-Based Filtering** – Users can filter files based on predefined categories.  

📌 **Core Functions:**  
- `browse_directory()` → Opens a file selection dialog.  
- `list_files()` → Displays all files within the selected directory.  
- `sort_files()` → Sorts files based on name, size, type, or last modified date.  
- `apply_category_filter()` → Filters files into categories (Documents, Images, Videos, etc.).  

✔ **This module ensures a clean and intuitive user experience.**  

---

### **🔹 Module 2: File Operations & Metadata Extraction**  
📌 **Purpose:**  
This module handles **file management operations** such as opening, renaming, deleting files, and extracting metadata like size, creation date, modification date, and last accessed date.  

📌 **Key Components:**  
✅ **File Operations** – Provides users with full control over files.  
✅ **Metadata Extraction** – Retrieves essential file details.  
✅ **Safe File Deletion** – Includes a confirmation prompt before deleting files.  

📌 **Core Functions:**  
- `open_file()` → Opens the selected file with its default application.  
- `rename_file()` → Renames the selected file with user input.  
- `delete_file()` → Deletes the selected file after user confirmation.  
- `view_metadata()` → Calls `metadata_extractor.py` to fetch file properties.  

📌 **Metadata Extraction (`metadata_extractor.py`):**  
- Uses `os.path.getsize()` to get file size.  
- Uses `time.ctime(os.path.getmtime())` to retrieve timestamps.  
- Extracts **file type, creation date, modification date, and last accessed date**.  

✔ **This module ensures efficient file management with detailed metadata retrieval.**  

---

### **🔹 Module 3: File Sorting & Categorization**  
📌 **Purpose:**  
This module focuses on **sorting and structuring files** based on user-defined attributes and **categorizing** them into different types.  

📌 **Key Components:**  
✅ **Sorting Mechanism** – Sorts files based on name, size, type, or last modified date.  
✅ **File Categorization** – Classifies files into groups like Documents, Images, Videos, etc.  

📌 **Core Functions:**  
- `sort_files()` → Sorts files based on selected criteria.  
- `apply_category_filter()` → Filters files based on type.  
- `get_category()` → Determines file type based on its extension.  

📌 **Sorting Implementation:**  
✅ Uses a dropdown menu (`QComboBox`) for sorting options.  
✅ Sorting logic is implemented using Python’s `sorted()` function.  

```python
def sort_files(self):
    sort_option = self.sort_by_dropdown.currentText()
    if sort_option == "Size":
        self.files_data.sort(key=lambda x: x[1], reverse=True)  # Sort by size
    elif sort_option == "Last Modified":
        self.files_data.sort(key=lambda x: x[4], reverse=True)  # Sort by date
```
## 📌 Contributing Guidelines  

We welcome contributions to improve the **AI-Powered Directory Management System**! Follow these guidelines to ensure a smooth and efficient process.  

---

## 🔹 How to Contribute?  

### 1️⃣ Fork the Repository  
- Click the "Fork" button on the top right of the GitHub repository.  
- This will create a copy of the repository under your GitHub account.  

### 2️⃣ Clone Your Forked Repository  
- Run the following command in your terminal:  
```sh
git clone https://github.com/Sakura-winter/Dir_manager.git
cd Dir_manager
```
### 3️⃣ Create a New Branch  
- Always create a separate branch for new features or fixes:
```sh
git checkout -b feature-new-enhancement
```
### 4️⃣ Make Your Changes
- Edit the code and add your improvements.
- Ensure your code follows the existing coding standards.
- Run tests before committing changes.
### 5️⃣ Commit Your Changes
- Write clear and meaningful commit messages:
```sh
git add .
git commit -m "Added new feature: [describe the feature]"
```
### 6️⃣ Push to GitHub
- Push your changes to your forked repository:
```sh
git push origin feature-new-enhancement
```
### 7️⃣ Open a Pull Request (PR)
- Go to the original repository on GitHub.
- Click on "Pull Requests" → "New Pull Request".
- Select your branch and submit the PR with a clear title and description.

## 📌 Future Enhancements  

The **AI-Powered Directory Management System** is designed to be scalable and extendable. Below are some planned future enhancements:  

### 🔹 **1. AI-Powered File Categorization**  
- Implement **Machine Learning (ML)** to categorize files based on **content, not just extensions**.  
- Use **Natural Language Processing (NLP)** to classify text files intelligently.  

### 🔹 **2. OCR-Based Text Extraction**  
- Integrate **Optical Character Recognition (OCR)** to extract text from **scanned images and PDFs**.  
- Enable **search functionality** based on extracted text.  

### 🔹 **3. Duplicate File Finder**  
- Detect **duplicate files** using **hashing techniques (MD5, SHA-256)**.  
- Provide an option to **merge, delete, or archive** duplicate files.  

### 🔹 **4. File Preview Feature**  
- Allow users to preview **text files, PDFs, and images** without opening them in external applications.  
 

### 🔹 **5. Advanced File Search**  
- Implement a **fuzzy search algorithm** to find files quickly, even with minor spelling errors.  

### 🔹 **6. Automation Features**  
- Set up **automated file cleanup** based on user-defined rules.  
- Implement **scheduled backups** to prevent accidental data loss.

### 🔹 **7. Long-Term Vision**  
- Extend this project into an **AI-driven smart file manager** with advanced **predictive organization**.  
- Integrate **voice commands & automation scripts** for seamless user experience.  

---

### ✅ **These features will make the project even more powerful and user-friendly in the future!** 🚀  


## 📌 Author & Acknowledgments  

👤 **Author:**  
- **Sumit Kumar Mehta (@Sakura-winter)** – Developer & Maintainer  

📢 **Acknowledgments:**  
I would like to express my sincere gratitude to **Prof. Navjot Kaur** for assigning this project and providing valuable guidance throughout its development.  

This project was a great learning experience, allowing me to apply my technical skills and explore AI-based file management.  


💡 **Thank you for your support and guidance!** 🚀  









