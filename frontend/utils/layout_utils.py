from PyQt5.QtWidgets import (
    QHBoxLayout, 
    QVBoxLayout,
    QWidget,
    QMessageBox
)

from views.main_window_view import MainWindow

# Function to add widget to layout
def addWidgetToLayout(widget:QWidget, layout:QHBoxLayout | QVBoxLayout):
    layout.addWidget(widget)

# Function to add child layout to parent layout
def addChildLayoutToParentLayout(childLayout: QHBoxLayout | QVBoxLayout, mainLayout: QHBoxLayout | QVBoxLayout):
    mainLayout.addLayout(childLayout)

def addInformationMsgBox(mainWindow: MainWindow, title: str, msg: str):
    QMessageBox.information(mainWindow, title, msg)

def addCriticalMsgBox(mainWindow: MainWindow, title: str, msg: str):
    QMessageBox.critical(mainWindow, title, msg)

def addWarningMsgBox(mainWindow: MainWindow, title: str, msg: str):
    QMessageBox.warning(mainWindow, title, msg)