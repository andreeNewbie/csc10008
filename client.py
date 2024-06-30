from dotenv import load_dotenv
import sys
from PyQt6.QtWidgets import QApplication, QStackedWidget

from ui import Login_w, SignUp_w

load_dotenv()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_page = Login_w()
    signup_page = SignUp_w()

    # allow multiple windows to be managed
    stack_widget = QStackedWidget()
    stack_widget.addWidget(login_page)
    stack_widget.addWidget(signup_page)

    # handle switch page
    login_page.signUpButton.clicked.connect(
        lambda: stack_widget.setCurrentIndex(1)
    )
    signup_page.loginButton.clicked.connect(
        lambda: stack_widget.setCurrentIndex(0)
    )

    # set the current (default) first added (login_w)
    stack_widget.setCurrentIndex(0)
    stack_widget.setFixedHeight(500)
    stack_widget.setFixedWidth(700)
    stack_widget.show()

    sys.exit(app.exec())
