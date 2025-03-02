from PyQt5.QtWidgets import (
    QMainWindow, 
    QApplication,
    QStackedWidget
)
from models.target_model import TargetModel
from views.main_menu_view import MainMenuView
from views.harden_target_menu_view import HardenTargetMenuView
from views.patch_target_menu_view import PatchTargetMenuView
from views.target_list_menu_view import TargetListMenuView
from controllers.main_menu_controller import MainMenuController
from controllers.harden_target_menu_controller import HardenTargetMenuController
from controllers.patch_target_menu_controller import PatchTargetMenuController
from controllers.target_list_menu_controller import TargetListMenuController

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SECOR")

        self.model = TargetModel()

        self.mainMenuView = MainMenuView()
        self.hardenTargetMenuView = HardenTargetMenuView()
        self.patchTargetMenuView = PatchTargetMenuView()
        self.targetListMenuView = TargetListMenuView()

        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(self.mainMenuView)
        self.stackedWidget.addWidget(self.hardenTargetMenuView)
        self.stackedWidget.addWidget(self.patchTargetMenuView)
        self.stackedWidget.addWidget(self.targetListMenuView)
        self.setCentralWidget(self.stackedWidget)
        
        self.mainMenuController = MainMenuController(self.mainMenuView, self.model, self)
        self.hardenTargetMenuController = HardenTargetMenuController(self.hardenTargetMenuView, self.model, self)
        self.patchTargetMenuController = PatchTargetMenuController(self.patchTargetMenuView, self.model, self)
        self.targetListMenuController = TargetListMenuController(self.targetListMenuView, self.model, self)

        self.switchToMainMenu()
        self.show()

    def switchToMainMenu(self):
        self.setWindowTitle("SECOR - Main Menu")
        self.stackedWidget.setCurrentWidget(self.mainMenuView)

    def switchToHardenTargetMenu(self):
        self.setWindowTitle("SECOR - Harden Menu")
        self.stackedWidget.setCurrentWidget(self.hardenTargetMenuView)
    
    def switchToPatchTargetMenu(self):
        self.setWindowTitle("SECOR - Patch Menu")
        self.stackedWidget.setCurrentWidget(self.patchTargetMenuView)

    def switchToTargetListMenu(self):
        self.setWindowTitle("SECOR - Target List Menu")
        self.stackedWidget.setCurrentWidget(self.targetListMenuView)

if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()