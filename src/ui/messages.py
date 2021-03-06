from PyQt5.QtWidgets import QMessageBox
from entities.notification import Notification
import plyer
import os
import platform


def error(title, message):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText(message)
    msg.setWindowTitle(title)
    msg.exec_()


def success(title, message):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(message)
    msg.setWindowTitle(title)
    msg.exec_()


def notify(notification: Notification):
    img_path = os.getcwd()

    if platform.system() == "Linux":
        img_path = f"{img_path}/img/icon.png"
    elif platform.system() == "Windows":
        img_path = f"{img_path}/img/icon.ico"

    plyer.notification.notify(
        title=notification.title,
        message=notification.message,
        timeout=20,
        app_name="TaskForce",
        app_icon=img_path
    )
