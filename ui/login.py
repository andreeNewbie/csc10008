from PyQt6 import uic
from PyQt6.QtWidgets import *

from .components import Success_w

from db import user_col as User

class Login_w(QMainWindow):
    def __init__ (self):
        super(Login_w, self).__init__()
        uic.loadUi("templates/login.ui", self)
        
    def login(self):
        name = self.userName.text()
        pw = self.userPassword.text()
        data = {"name": name, "passWord": pw}
        if(User.find_one(data)):
            Success_w().show()
        else:
            self.show_error_window()  # Show error window for incorrect credentials
    
    def show_error_window(self):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Icon.Warning)
        error_dialog.setText("USER OR PASSWORD IS WRONG TRY AGAIN!")
        error_dialog.setWindowTitle("Login Error")
        error_dialog.exec()