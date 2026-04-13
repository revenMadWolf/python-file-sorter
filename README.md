# 📁 Smart File Organizer (GUI)

A simple and efficient desktop application that automatically organizes files in a selected folder based on their file types.

Built using **Python** and **PySide6 (Qt Designer)**.

---

## 🚀 Features

* 📂 Select any folder from your system
* 🗂 Automatically sort files into categories:

  * Images
  * Documents
  * Videos
  * Audio
  * Archives
  * Others
* 🧾 Real-time log output showing file movements
* 🖥 Clean GUI built with Qt Designer
* ⚡ Fast and lightweight

---

## 🛠 Tech Stack

* **Python 3**
* **PySide6** (GUI framework)
* **Qt Designer** (UI design)
* **os / shutil** (file handling)

---

## 📦 Project Structure

```
python-file-organizer/
│
├── main.py          # GUI logic
├── functions.py     # File organizing logic
├── main.ui          # UI layout (Qt Designer)
└── README.md
```

---

## ▶️ How to Run

1. Clone the repository:

```
git clone https://github.com/revenMadWolf/python-file-organizer.git
cd python-file-organizer
```

2. Install dependencies:

```
pip install pyside6
```

3. Run the application:

```
python main.py
```

---

## 🧠 How It Works

* The user selects a folder
* The program scans all files inside it
* Files are categorized based on their extensions
* Corresponding folders are created automatically
* Files are moved into their respective folders

---

## ⚠️ Notes

* Existing folders are reused (no duplicates created)
* Files with duplicate names may be skipped
* It is recommended to test on a non-critical folder first

---

## 🔮 Future Improvements

* [ ] Handle duplicate file names (auto-rename)
* [ ] Allow users to create custom file categories with their own extensions
* [ ] Progress bar for large folders
* [ ] Undo functionality
* [ ] Drag & drop folder support

---

## 📸 Screenshots

*(Add screenshots of your UI here later)*

---

## 💡 Motivation

This project was built to practice:

* GUI development with PySide6
* File system automation
* Writing clean, modular Python code

---

## 📜 License

This project is open-source and available under the MIT License.
