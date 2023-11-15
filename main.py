import sys
from PyQt5.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog, QMainWindow)

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

        # add widgets
        self.nameBox = QLineEdit("First Name")
        self.nameBox.setMinimumSize(100,50)


        self.lastNameBox = QLineEdit("Last Name")

        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.nameBox, stretch=1)
        layout.addWidget(self.lastNameBox, stretch=3)
        

        self.setLayout(layout)






if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form2()
    #form.show()

    window = QMainWindow()
    window.addWidget(form)
    window.resize(500, 500)
    window.show()
    # Run the main Qt loop
    sys.exit(app.exec())