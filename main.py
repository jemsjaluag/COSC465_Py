import sys
from login import Login
from pathlib import Path
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from signup import Form2


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create and show the login form
    loginForm = Login()
    loginForm.show()

    # Run the main Qt loop
    sys.exit(app.exec())