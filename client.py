import socket

from dotenv import load_dotenv
import sys
from PyQt6.QtWidgets import QApplication, QStackedWidget

from ui import Login_w, SignUp_w, HomePage_w

load_dotenv()

HOST = "127.0.0.1"  # localhost
PORT = 3000

print("CLIENT SIDE: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print("Client", HOST, client_socket.getsockname())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_page = Login_w()
    signup_page = SignUp_w()
    home_page = HomePage_w()

    # Allow multiple windows to be managed
    stack_widget = QStackedWidget()
    stack_widget.addWidget(login_page)
    stack_widget.addWidget(signup_page)
    stack_widget.addWidget(home_page)

    # Handle switch page
    login_page.signUpButton.clicked.connect(lambda: stack_widget.setCurrentIndex(1))
    signup_page.loginButton.clicked.connect(lambda: stack_widget.setCurrentIndex(0))
    login_page.login_successful.connect(lambda: stack_widget.setCurrentIndex(2))

    stack_widget.setCurrentIndex(0)
    stack_widget.setFixedHeight(600)
    stack_widget.setFixedWidth(800)
    stack_widget.show()

    sys.exit(app.exec())
