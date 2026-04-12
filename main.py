from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        ui_file = QFile("main.ui")
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        self.setCentralWidget(self.ui.centralWidget())

        # Connect buttons
        self.ui.btn_select_folder.clicked.connect(self.select_folder)
        self.ui.btn_organize.clicked.connect(self.organize_files)

        self.folder_path = ""

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            self.folder_path = folder
            self.ui.lbl_path.setText(folder)

    def organize_files(self):
        if not self.folder_path:
            self.ui.txt_log.append("No folder selected!")
            return

        self.ui.txt_log.append("Organizing files...")
        # logic will come later


app = QApplication([])
window = MainWindow()
window.show()
app.exec()