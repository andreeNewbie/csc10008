from dotenv import load_dotenv
import sys
from PyQt6.QtWidgets import QApplication, QStackedWidget

from ui import Login_w, SignUp_w, Success_w

load_dotenv()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # allow multiple windows to be managed
    widget = QStackedWidget()
    widget.addWidget(Login_w())
    widget.addWidget(SignUp_w())
    widget.addWidget(Success_w())
    # set the current (default) first added (login_w)
    widget.setCurrentIndex(0)
    widget.setFixedHeight(500)
    widget.setFixedWidth(700)
    widget.show()

    sys.exit(app.exec())
