from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QFileDialog


class HomePage_w(QMainWindow):

    def __init__(self):
        super(HomePage_w, self).__init__()
        uic.loadUi("templates/home_page.ui", self)
        self.chooseFileButton.clicked.connect(self.click_handler)

    def click_handler(self):
        dialog = QFileDialog()
        dialog.setNameFilter("All files (*.png, *.txt)")
        dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        dialog_success = dialog.exec()

        if dialog_success == 1:
            selected_file_path = dialog.selectedFiles()
            file_name = self.getName(selected_file_path[0])
            self.fileName.setText(file_name)

    def getName(self, selected_file_path):
        index = 0
        cnt = len(selected_file_path) - 1
        file_name = ""
        while cnt >= 0:
            if selected_file_path[cnt] == "/":
                index = cnt + 1
                break
            cnt -= 1

        while index < len(selected_file_path):
            file_name += selected_file_path[index]
            index += 1
        return file_name
