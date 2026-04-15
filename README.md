# 📁 Python File Sorter

A desktop file organizer built with **Python** and **PySide6** that automatically sorts files into categories based on their extensions.

This project was created as a practical tool and a portfolio project to demonstrate GUI development, file handling, and clean code structure.

---

## 🚀 Features

* 📂 Select any folder and organize its files
* 🧠 Custom categories (Images, Documents, Videos, etc.)
* 📝 Editable categories via GUI
* 🔁 Duplicate handling:

  * Skip duplicates
  * Or auto-rename them
* 📦 Optional **"Others"** folder for uncategorized files
* 💾 Saves settings using JSON (`file_types.json`)
* 🖥️ Built with Qt Designer + PySide6

---

## 📸 Preview

![img_1.png](img_1.png)
![img_2.png](img_2.png)

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/revenMadWolf/python-file-manager.git
cd python-file-manager
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv .venv
```

### 3. Activate it

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux/Mac:**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install PySide6
```

---

## ▶️ Usage

Run the app:

```bash
python main.py
```

### Steps:

1. Click **"Select Folder"**
2. Choose a directory
3. (Optional):

   * Enable **Rename duplicates**
   * Enable **Add other file**
4. Click **"Organize Files"**

---

## 🧩 Custom Categories

Click **"Customize"** to define file types.

### Example:

```
Images → .jpg, .png, .jpeg
Documents → .pdf, .txt, .docx
```

These are saved in:

```
file_types.json
```

---

## 📂 Project Structure

```
python-file-manager/
│
├── main.py              # GUI logic (PySide6)
├── functions.py         # File organization logic
├── main.ui              # UI design (Qt Designer)
├── file_types.json      # Saved categories
└── README.md
```

---

## ⚠️ Notes

* File extensions are matched case-insensitively
* Extensions needs to be typed in with "." in front. (✅.png, .mp3   ❌png, mp3)
* Existing files are not overwritten unless rename is enabled
* Works best on Windows (tested environment)

---

## 🧠 What I Learned

* Building GUI apps with PySide6
* Working with file systems (`os`, `shutil`)
* JSON-based configuration handling
* Structuring a real-world Python project

---

## 📜 Author

* Thisew Nethmira
