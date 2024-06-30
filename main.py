from dotenv import load_dotenv
import os

from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi 
import sys
import pymongo

load_dotenv()

#check if connect to database or not
try:
    myClient = pymongo.MongoClient(os.getenv('MONGODB_URL'))
    clientDB = myClient["users"]
    clientCol = clientDB["userData"]
    print("Connected to MongoDB successfully!")
except pymongo.errors.ConnectionFailure as e:
    print(f"Failed to connect to MongoDB: {e}")


class Login_w(QMainWindow):
    def __init__ (self):
        super(Login_w, self).__init__()
        uic.loadUi("login.ui", self)
        
    def login(self):
        name = self.userName.text()
        pw = self.userPassword.text()
        data = {"name": name, "passWord": pw}
        if(clientCol.find_one(data)):
            Success_w().show()
        else:
            self.show_error_window()  # Show error window for incorrect credentials
    
    def show_error_window(self):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Icon.Warning)
        error_dialog.setText("USER OR PASSWORD IS WRONG TRY AGAIN!")
        error_dialog.setWindowTitle("Login Error")
        error_dialog.exec()
        
    
    
    
class SignUp_w(QMainWindow):
    def __init__ (self):
        super(SignUp_w, self).__init__()
        uic.loadUi("signUp.ui", self)

class Success_w(QMainWindow):
    def __init__ (self):
        super(Success_w, self).__init__()
        uic.loadUi("success.ui", self)

app  = QApplication(sys.argv)
widget = QStackedWidget() #allow multiple windows to be managed
login_f = Login_w()
signUp_f = SignUp_w()
success_f = Success_w()
widget.addWidget(login_f)
widget.addWidget(signUp_f)
widget.addWidget(success_f)
widget.setCurrentIndex(0) #set the current (default) first added (login_w)
widget.setFixedHeight(500)
widget.setFixedWidth(700)
widget.show()
app.exec()