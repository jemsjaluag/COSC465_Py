import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


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

        self.setGeometry(100,100,400,500)
        self.formGroupBox = QGroupBox("Signup")

        ##### add widgets
        # username
        self.usernameLabel = QLabel("Username")
        self.usernameLabel.setFrameStyle(QFrame.Sunken)
        self.usernameLabel.setAlignment(Qt.AlignBottom | Qt.AlignLeft)

        self.userName = QLineEdit()
        self.userName.setMinimumSize(textBoxWidth,textBoxHeight)
        self.userName.move(20,20)
        self.usernameLabel.setBuddy(self.userName)

        # password
        self.passwordLabel = QLabel("Password")
        self.password = QLineEdit()
        self.password.setMinimumSize(textBoxWidth,textBoxHeight)

        # first name
        self.nameBox = QLineEdit("First Name")
        self.nameBox.setMinimumSize(textBoxWidth,textBoxHeight)

        # last name
        self.lastNameBox = QLineEdit("Last Name")
        self.lastNameBox.setMinimumSize(textBoxWidth,textBoxHeight)

        # preferred sport
        self.preferredSport = QLineEdit("Preferred Sport")
        self.preferredSport.setMinimumSize(textBoxWidth,textBoxHeight)

        # age
        self.age = QLineEdit("Age") 
        self.age.setMinimumSize(textBoxWidth,textBoxHeight)

        # creating the form layout
        formLayout = QFormLayout()
        formLayout.addRow(self.usernameLabel, self.userName)
        formLayout.addRow(self.passwordLabel, self.password)

        self.formGroupBox.setLayout(formLayout)

        # button
        self.button = QPushButton("Submit")
        buttonX = self.button.x()
        buttonY = self.button.y()
        self.button.setMaximumSize(80, 40)
        self.button.move(maxWidth / 2, maxHeight)

        # create form
        #self.createForm()

        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.formGroupBox)

        """
        layout.addWidget(self.usernameLabel)
        layout.addWidget(self.nameBox)
        layout.addWidget(self.lastNameBox)
        layout.addWidget(self.userName)
        layout.addWidget(self.password)
        layout.addWidget(self.preferredSport)
        layout.addWidget(self.age)
        layout.addWidget(self.button)
        """

        self.setLayout(layout)






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