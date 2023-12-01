import sys
from pathlib import Path
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget

class Login(QDialog):

    def __init__(self, parent=None):
        super(Login, self).__init__(parent)

        ###### stylesheets
        self.setStyleSheet(Path('signup.qss').read_text())

        self.windowWidth = 400
        self.windowHeight = 300

        textBoxWidth = 80
        textBoxHeight = 30

        self.setGeometry(100,100,self.windowWidth,self.windowHeight)
        self.formGroupBox = QGroupBox("Login") 

        ##### login label
        self.loginLabel = QLabel("Login")
        self.loginLabel.setGeometry(100,100,100,100)
        self.loginLabel.setAlignment(Qt.AlignCenter)
        self.loginLabel.setObjectName('loginLabel')

        ##### login subheading
        self.loginSubheading = QLabel("Please login with your account",
                                      alignment=Qt.AlignCenter)
        
        ###### username
        self.usernameBox = QLineEdit()
        self.usernameBox.setPlaceholderText("Username")
        self.usernameBox.setMinimumSize(textBoxWidth,textBoxHeight)
        self.usernameBox.setMaxLength(20)

        #####
        self.passwordBox = QLineEdit()
        self.passwordBox.setPlaceholderText("Password")
        self.passwordBox.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordBox.setMaxLength(20)

        ##### button
        self.button = QPushButton("Login")
        #self.button.setMaximumSize(150,50)
        self.button.setFixedSize(150,50)

        ###### create the format
        self.__createFormFormat()

        ##### main layout
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.formGroupBox)
        self.mainLayout.addWidget(self.button, alignment=Qt.AlignCenter | Qt.AlignBottom)

        ##### main layout of the window/widget
        self.setLayout(self.mainLayout)
    


    def __createFormFormat(self):

        # init layout
        self.formLayout = QFormLayout()
        self.formLayout.setSpacing(20)

        # create separate vbox for login labels
        self.loginVBox = QVBoxLayout()
        self.loginVBox.addWidget(self.loginLabel)
        self.loginVBox.addWidget(self.loginSubheading)
        self.loginVBox.setSpacing(1)
        self.loginVBox.setObjectName('loginVbox')

        self.formLayout.addRow(self.loginVBox)
        self.formLayout.addRow(self.usernameBox)
        self.formLayout.addRow(self.passwordBox)

        self.formGroupBox.setLayout(self.formLayout)

