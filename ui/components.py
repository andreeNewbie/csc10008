from PyQt6 import uic
from PyQt6.QtWidgets import *


class Success_w(QMainWindow):
    def __init__ (self):
        super(Success_w, self).__init__()
        uic.loadUi("templates/success.ui", self)