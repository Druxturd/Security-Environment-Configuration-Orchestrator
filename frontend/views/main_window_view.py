from PySide6.QtWidgets import (
    QMainWindow,
    QStackedWidget
)
from pages import Page

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.stacked_widget = QStackedWidget()

    def switch_to_main_menu(self):
        self.setWindowTitle("SECOR - Main Menu")
        self.stacked_widget.setCurrentIndex(Page.MAIN_MENU)

    def switch_to_target_list_menu(self):
        self.setWindowTitle("SECOR - Target List Menu")
        self.stacked_widget.setCurrentIndex(Page.TARGET_LIST_MENU)

    def switch_to_harden_target_menu(self):
        self.setWindowTitle("SECOR - Harden Menu")
        self.stacked_widget.setCurrentIndex(Page.HARDEN_TARGET_MENU)

    def switch_to_patch_target_menu(self):
        self.setWindowTitle("SECOR - Patch Menu")
        self.stacked_widget.setCurrentIndex(Page.PATCH_TARGET_MENU)