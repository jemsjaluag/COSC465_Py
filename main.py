import sys
from pathlib import Path
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


# window dimensions
maxWidth = 500; maxHeight = 600

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Create widgets
        self.edit = QLineEdit("Write my name here")
        self.button = QPushButton("Show Greetings")
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.button.clicked.connect(self.greetings)

    # Greets the user
    def greetings(self):
        print(f"Hello Hello Hello{self.edit.text()}")


class Form2(QDialog):

    def __init__(self, parent=None):
        super(Form2, self).__init__(parent)

        ##### stylesheets
        self.setStyleSheet(Path('signup.qss').read_text())
        
        textBoxWidth = 80
        textBoxHeight = 30

        ### buffer for user info

        self.setGeometry(100,100,400,500)
        self.formGroupBox = QGroupBox("Signup")


        ##### add widgets
        # username
        self.usernameLabel = QLabel("Username")
        font = QFont("Calibri", 13)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setFrameStyle(QFrame.Sunken)
        self.usernameLabel.setAlignment(Qt.AlignBottom | Qt.AlignLeft)

        self.usernameLine = QLineEdit()
        self.usernameLine.setMinimumSize(textBoxWidth,textBoxHeight)

        ### password
        self.passwordLabel = QLabel("Password")
        self.passwordLine = QLineEdit()
        self.passwordLine.setMinimumSize(textBoxWidth,textBoxHeight)

        ### first name
        self.nameBox = QLineEdit("First Name")
        self.nameBox.setMinimumSize(textBoxWidth,textBoxHeight)

        ### last name
        self.lastNameBox = QLineEdit("Last Name")
        self.lastNameBox.setMinimumSize(textBoxWidth,textBoxHeight)

        ### preferred sport
        self.preferredSport = QLineEdit("Preferred Sport")
        self.preferredSport.setMinimumSize(textBoxWidth,textBoxHeight)

        ### age
        self.age = QLineEdit("Age") 
        self.age.setMinimumSize(textBoxWidth,textBoxHeight)

        # creating the form layout
        self.createFormFormat()
        
        ### button
        self.button = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button.centerButtons()
        self.button.accepted.connect(self.getInfo)
        self.button.move(300,300)

        # main layout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(self.button)

        self.setLayout(mainLayout)


    ### creates the form format
    def createFormFormat(self):
        formLayout = QFormLayout()
        formLayout.addRow(self.usernameLabel, self.usernameLine)
        formLayout.addRow(self.passwordLabel, self.passwordLine)

        self.formGroupBox.setLayout(formLayout)

    def getInfo(self):
        username = self.usernameLine.text()
        print(username)



if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form2()

    """
    window = QMainWindow()
    window.setCentralWidget(form)
    window.setGeometry(750,200,500, 600)
    window.setWindowTitle("elmao")
    """
    
    #window.show()
    form.show()

    # Run the main Qt loop
    sys.exit(app.exec())