import sys
from pathlib import Path
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


# window dimensions
maxWidth = 500; maxHeight = 500

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

        self.setGeometry(100,100,400,350)
        self.formGroupBox = QGroupBox("Signup")


        ########### add widgets
        ##### username
        self.usernameLabel = QLabel("Username")
        self.usernameLabel.setFrameStyle(QFrame.Sunken)
        self.usernameLabel.setAlignment(Qt.AlignBottom | Qt.AlignLeft)

        self.usernameLine = QLineEdit()
        self.usernameLine.setMinimumSize(textBoxWidth,textBoxHeight)
        self.usernameLine.setMaxLength(20)

        ##### password
        self.passwordLabel = QLabel("Password")
        self.passwordLine = QLineEdit()
        self.passwordLine.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordLine.setMinimumSize(textBoxWidth,textBoxHeight)
        self.passwordLine.setMaxLength(20)

        ##### first name
        self.nameBox = QLineEdit()
        self.nameBox.setPlaceholderText("First Name")
        self.nameBox.setMinimumSize(textBoxWidth,textBoxHeight)
        self.nameBox.setMaxLength(20)

        ##### last name
        self.lastNameBox = QLineEdit()
        self.lastNameBox.setPlaceholderText("Last Name")
        self.lastNameBox.setMinimumSize(textBoxWidth,textBoxHeight)
        self.lastNameBox.setMaxLength(20)

        ##### preferred sport
        self.preferredSport = QComboBox()
        self.preferredSport.setPlaceholderText("Preferred Sport")
        self.preferredSport.setMinimumSize(textBoxWidth,textBoxHeight)

        ##### age
        self.age = QLineEdit() 
        self.age.setMinimumSize(textBoxWidth,textBoxHeight)
        self.age.setPlaceholderText("Age")
        self.age.setMaxLength(3)

        ### warning text
        self.warningText = QLabel("test text")
        self.warningText.setObjectName("warning")

        # creating the form layout
        self.createFormFormat()
        
        ### button
        self.button = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button.centerButtons()

        # when OK is clicked, execute selfInfo func
        self.button.accepted.connect(self.getInfo)

        # when Cancel is clicked
        self.button.rejected.connect(self.reject)
        self.button.move(300,300)

        # main layout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(self.button)

        self.setLayout(mainLayout)


    ### creates the form format
    def createFormFormat(self):
        formLayout = QFormLayout()
        formLayout.setSpacing(12)

        # separate hbox for the name
        nameHBox = QHBoxLayout()
        nameHBox.addWidget(self.nameBox)
        nameHBox.addWidget(self.lastNameBox)

        formLayout.addRow(self.usernameLabel, self.usernameLine)
        formLayout.addRow(self.passwordLabel, self.passwordLine)
        formLayout.addRow(nameHBox)
        formLayout.addRow(self.age)
        formLayout.addRow(self.preferredSport)
        formLayout.addRow(self.warningText)

        self.extractSportList()

        self.formGroupBox.setLayout(formLayout)

    ### get the string from line edits
    def getInfo(self):
        enteredUsername = self.usernameLine.text()
        enteredPassword = self.passwordLine.text()
        enteredName = self.nameBox.text()
        enteredLast = self.lastNameBox.text()
        enteredPreferredSport = self.preferredSport.currentText()

        ### value error handling
        try:
            enteredAge = int(self.age.text())
            # age check
            if enteredAge < 18:
                self.warningText.setText("Age Warning: Below 18")
        
            print(f"{enteredUsername}\n{enteredPassword}\n{enteredName}\n" \
                + f"{enteredLast}\n{enteredPreferredSport}\n{enteredAge}")
            
        except ValueError as vE:
            self.warningText.setText("Invalid Age")

    ### extracts sport from the txt file
    def extractSportList(self):
        print("stuff")
        file = open("sports.txt", "r")
        while True:
            sport = file.readline()
            if not sport:
                break
            ### action
            # trim the string first, remove the \n
            sport = sport.rstrip("\n")
            self.preferredSport.addItem(sport)
        file.close()




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