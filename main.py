from PySide6.QtWidgets import QApplication,QFileDialog,QTableWidgetItem
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
    is_other_active = window.check_other.isChecked()
    is_rename_active = window.check_rename.isChecked()
    if selected_file:
        changes = functions.organize_files(selected_file,is_other_active,is_rename_active)
        for change in changes:
            window.txt_log.append(change)
    else:
        window.txt_log.append("No folder selected.")

def load_table():
    window.stackedWidget.setCurrentWidget(window.page_customize)
    data = functions.load_file_types()

    table = window.table_categories
    table.setRowCount(0)

    for row, (category, extensions) in enumerate(data.items()):
        table.insertRow(row)

        table.setItem(row, 0, QTableWidgetItem(category))
        table.setItem(row, 1, QTableWidgetItem(", ".join(extensions)))

def add_category():
    table = window.table_categories
    row_count = table.rowCount()
    table.insertRow(row_count)


def save_category():
    data_dic = {}
    table = window.table_categories
    for row in range(table.rowCount()):
        column = table.item(row,0)
        record = table.item(row,1)

        if column.text() and record.text():
            data_dic[column.text()] = [rec.strip() for rec in (record.text()).split(",") if rec.strip()]
    functions.save_file_types(data_dic)
    load_table()

def load_mainPage():
    window.stackedWidget.setCurrentWidget(window.page_main)


app = QApplication([])
loader = QUiLoader()
ui_file = QFile("main.ui")
ui_file.open(QFile.ReadOnly)

window = loader.load(ui_file)
window.setWindowTitle("File Manager")
# window.setGeometry(0,0,740,600)
window.setFixedSize(window.size())

ui_file.close()
window.show()

window.btn_select_folder.clicked.connect(select_folder)
window.btn_organize.clicked.connect(organize_files)
window.btn_customize.clicked.connect(load_table)

window.btn_slot.clicked.connect(add_category)
window.btn_save.clicked.connect(save_category)
window.btn_back.clicked.connect(load_mainPage)


app.exec()

