from PySide6.QtWidgets import QApplication,QFileDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
import functions


selected_file = ''

def select_folder():
    global selected_file
    selected_file = QFileDialog.getExistingDirectory(None,"Select Folder")

    if selected_file:
        window.lbl_path.setText(selected_file)
        window.txt_log.append(f"Selected: {selected_file}")

def organize_files():
    global selected_file
    if selected_file:
        changes = functions.organize_files(selected_file)
        for change in changes:
            window.txt_log.append(change)


app = QApplication([])
loader = QUiLoader()
ui_file = QFile("main.ui")
ui_file.open(QFile.ReadOnly)

window = loader.load(ui_file)
window.setWindowTitle("File Manager")
window.setGeometry(800,500,800,500)

ui_file.close()
window.show()

window.btn_select_folder.clicked.connect(select_folder)
window.btn_organize.clicked.connect(organize_files)
app.exec()

