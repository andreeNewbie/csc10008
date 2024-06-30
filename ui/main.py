# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

from .login import Login_w

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 40, 361, 121))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 170, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 230, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.userName = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.userName.setGeometry(QtCore.QRect(230, 160, 391, 31))
        self.userName.setObjectName("userName")
        self.userPassword = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.userPassword.setGeometry(QtCore.QRect(230, 220, 391, 31))
        self.userPassword.setObjectName("userPassword")
        self.loginButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(310, 300, 93, 28))
        self.loginButton.setObjectName("loginButton")
        self.SignUpButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.SignUpButton.setGeometry(QtCore.QRect(310, 350, 93, 28))
        self.SignUpButton.setObjectName("SignUpButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.loginButton.clicked.connect(self.handleLogin)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "USER ACCOUNT"))
        self.label_2.setText(_translate("MainWindow", "UserName:"))
        self.label_3.setText(_translate("MainWindow", "Password:"))
        self.loginButton.setText(_translate("MainWindow", "LOGIN"))
        self.SignUpButton.setText(_translate("MainWindow", "SIGN UP"))

        
    def handleLogin(self):
        loginWindow = Login_w()
        loginWindow.login()