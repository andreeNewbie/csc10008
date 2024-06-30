from PyQt6 import uic
from PyQt6.QtWidgets import *

class SignUp_w(QMainWindow):
    def __init__ (self):
        super(SignUp_w, self).__init__()
        uic.loadUi("templates/sign_up.ui", self)