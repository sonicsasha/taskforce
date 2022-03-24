import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QErrorMessage, QMessageBox
from PyQt5.QtGui import QIcon
from taskforce_service import taskforce_service, WrongCredentials
import plyer

from ui.login_window_ui import Ui_LoginScreen

class loginWindow(QMainWindow, Ui_LoginScreen):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalSlots()
        self.setWindowTitle("TaskForce")
        self.setWindowIcon(QIcon("img/check-svgrepo-com.svg"))
        

    
    def connectSignalSlots(self):
        self.loginButton.pressed.connect(self.login)
        self.signupButton.pressed.connect(self.signup)

    def login(self):
        try:
            user = taskforce_service.login(self.usernameFill.text(), self.passwordFill.text())
            plyer.notification.notify(title="Logged in", message=f"Welcome {user.name}")
        except WrongCredentials:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("The username couldn't be found or the password is incorrect. Please try again!")
            msg.setWindowTitle("Error")
            msg.exec_()
    
    def signup(self):
        print("Signing up")