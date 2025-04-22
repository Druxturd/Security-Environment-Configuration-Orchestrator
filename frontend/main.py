import asyncio
import sys
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import (
    QMainWindow, 
    QApplication,
    QStackedWidget
)
from qasync import QEventLoop, asyncSlot
from models.target_model import TargetModel
from models.target_data_manager import TargetDataManager
from views.main_menu_view import MainMenuView
from views.harden_target_menu_view import HardenTargetMenuView
from views.patch_target_menu_view import PatchTargetMenuView
from views.target_list_menu_view import TargetListMenuView
from views.error_view import ErrorView
from controllers.main_menu_controller import MainMenuController
from controllers.harden_target_menu_controller import HardenTargetMenuController
from controllers.patch_target_menu_controller import PatchTargetMenuController
from controllers.target_list_menu_controller import TargetListMenuController

# Class for whole application window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initWindowConfig()
        self.initModels()
        self.initViews()
        self.initControllers()

        # To show main menu UI
        self.switchToMainMenu()

    # Function to configure the window of application
    def initWindowConfig(self):
        # Set window title
        self.setWindowTitle("SECOR")

        # Set fixed size
        self.setFixedSize(QSize(640, 480))

    # Function to init models that will be processed within application
    def initModels(self):
        # Set target model manager that will be processing data within application
        self.modelManager = TargetDataManager()

    # Function to init views / UI within application
    def initViews(self):
        """
        Set application views / UI which consist of 4 menus:
        1. Main Menu
        2. Target List Menu
        3. Harden Target Menu
        4. Patch Target Menu
        """
        self.mainMenuView = MainMenuView()
        self.targetListMenuView = TargetListMenuView()
        self.hardenTargetMenuView = HardenTargetMenuView()
        self.patchTargetMenuView = PatchTargetMenuView()

        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(self.mainMenuView)
        self.stackedWidget.addWidget(self.targetListMenuView)
        self.stackedWidget.addWidget(self.hardenTargetMenuView)
        self.stackedWidget.addWidget(self.patchTargetMenuView)
        self.setCentralWidget(self.stackedWidget)
        
    # Function to controllers / logic within application
    def initControllers(self):
        # Set application controllers which consist of logic for each view / mmenu
        self.mainMenuController = MainMenuController(self.mainMenuView, self.modelManager, self)
        self.targetListMenuController = TargetListMenuController(self.targetListMenuView, self.modelManager, self)
        self.hardenTargetMenuController = HardenTargetMenuController(self.hardenTargetMenuView, self.modelManager, self)
        self.patchTargetMenuController = PatchTargetMenuController(self.patchTargetMenuView, self.modelManager, self)

    # Function to show main menu UI
    def switchToMainMenu(self):
        self.setWindowTitle("SECOR - Main Menu")
        self.stackedWidget.setCurrentWidget(self.mainMenuView)

    # Function to show target list menu UI
    def switchToTargetListMenu(self):
        self.setWindowTitle("SECOR - Target List Menu")
        self.stackedWidget.setCurrentWidget(self.targetListMenuView)

    # Function to show harden target menu UI
    def switchToHardenTargetMenu(self):
        self.setWindowTitle("SECOR - Harden Menu")
        self.stackedWidget.setCurrentWidget(self.hardenTargetMenuView)
    
    # Function to show patch target menu UI
    def switchToPatchTargetMenu(self):
        self.setWindowTitle("SECOR - Patch Menu")
        self.stackedWidget.setCurrentWidget(self.patchTargetMenuView)

    # Function to show error dialog UI
    def showError(self, message):
        errorDialog = ErrorView(message)
        errorDialog.exec()

# Run the app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Security Environment Configuration Orchestrator")

    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    window = MainWindow()
    window.show()

    async def cleanup():
        print("Cleaning up...")

    with loop:
        try:
            loop.run_forever()
        finally:
            loop.run_until_complete(cleanup())
