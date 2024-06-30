from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox, QMainWindow

from db import user_col as User


class Login_w(QMainWindow):
    def __init__(self):
        super(Login_w, self).__init__()
        uic.loadUi("templates/login.ui", self)
        self.loginButton.clicked.connect(self.login)

    def login(self):
        name = self.userName.text()
        pw = self.userPassword.text()
        data = {"name": name, "password": pw}
        if User.find_one(data):
            self.show_success_window()
            self.userName = ""
            self.userPassword = ""
        else:
            self.show_error_window()

    def show_error_window(self):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Icon.Warning)
        error_dialog.setText("LOGIN FAIL !!!")
        error_dialog.setWindowTitle("Login Error")
        error_dialog.exec()

    def show_success_window(self):
        success_dialog = QMessageBox()
        success_dialog.setIcon(QMessageBox.Icon.Information)
        success_dialog.setText("LOGIN SUCCESS !!!")
        success_dialog.setWindowTitle("Notification")
        success_dialog.exec()
