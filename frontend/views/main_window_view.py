from PyQt5.QtWidgets import (
    QMainWindow, 
    QStackedWidget
)

from pages import Page

# Class for whole application window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.stacked_widget = QStackedWidget()

    # Function to show main menu UI
    def switchToMainMenu(self):
        self.setWindowTitle("SECOR - Main Menu")
        self.stacked_widget.setCurrentIndex(Page.MAIN_MENU)

    # Function to show target list menu UI
    def switchToTargetListMenu(self):
        self.setWindowTitle("SECOR - Target List Menu")
        self.stacked_widget.setCurrentIndex(Page.TARGET_LIST_MENU)

    # Function to show harden target menu UI
    def switchToHardenTargetMenu(self):
        self.setWindowTitle("SECOR - Harden Menu")
        self.stacked_widget.setCurrentIndex(Page.HARDEN_TARGET_MENU)
    
    # Function to show patch target menu UI
    def switchToPatchTargetMenu(self):
        self.setWindowTitle("SECOR - Patch Menu")
        self.stacked_widget.setCurrentIndex(Page.PATCH_TARGET_MENU)