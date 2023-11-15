import sys
from PyQt5.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog, QMainWindow)
from PyQt5.QtCore import QRect


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

        textBoxWidth = 80
        textBoxHeight = 30

        # add widgets

        self.userName = QLineEdit("Username")
        self.userName.setMinimumSize(textBoxWidth,textBoxHeight)

        self.password = QLineEdit("Password")
        self.password.setMinimumSize(textBoxWidth,textBoxHeight)

        self.nameBox = QLineEdit("First Name")
        self.nameBox.setMinimumSize(textBoxWidth,textBoxHeight)


        self.lastNameBox = QLineEdit("Last Name")
        self.lastNameBox.setMinimumSize(textBoxWidth,textBoxHeight)

        self.preferredSport = QLineEdit("Preferred Sport")
        self.preferredSport.setMinimumSize(textBoxWidth,textBoxHeight)

        self.age = QLineEdit("Age") 
        self.age.setMinimumSize(textBoxWidth,textBoxHeight)

        # button
        self.button = QPushButton("Submit")
        buttonX = self.button.x()
        buttonY = self.button.y()
        self.button.setMaximumSize(80, 40)
        self.button.move(maxWidth / 2, maxHeight)
        #self.button.setGeometry(buttonX,buttonY, 30, 80)


        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.nameBox)
        layout.addWidget(self.lastNameBox)
        layout.addWidget(self.userName)
        layout.addWidget(self.password)
        layout.addWidget(self.preferredSport)
        layout.addWidget(self.age)
        layout.addWidget(self.button)

        self.setLayout(layout)






if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form2()
    #form.show()

    window = QMainWindow()
    window.setCentralWidget(form)
    window.setFixedSize(500, 600)
    window.setWindowTitle("elmao")

    window.show()

    # Run the main Qt loop
    sys.exit(app.exec())