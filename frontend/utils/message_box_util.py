from views.main_window_view import MainWindow

from PyQt5.QtWidgets import QMessageBox

def addInformationMsgBox(mainWindow: MainWindow, title: str, msg: str):
    QMessageBox.information(mainWindow, title, msg)

def addCriticalMsgBox(mainWindow: MainWindow, title: str, msg: str):
    QMessageBox.critical(mainWindow, title, msg)

def addWarningMsgBox(mainWindow: MainWindow, title: str, msg: str):
    QMessageBox.warning(mainWindow, title, msg)