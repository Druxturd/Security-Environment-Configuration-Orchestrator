from views.main_menu_view import MainMenuView
from views.main_window_view import MainWindow

from models.target_data_manager import TargetDataManager

from utils.layout_utils import addWarningMsgBox

class MainMenuController:
    def __init__(self, view:MainMenuView, model_manager:TargetDataManager, main_window:MainWindow):
        # Store the view, model manager, main window that being passed into the controller
        self.view = view
        self.model_manager = model_manager
        self.main_window = main_window

        self.errorTitle = "Error"
        self.errorMsg = "Empty List!"

        # Set the initial total target counter
        self.view.totalTargetLbl.setText("Total Target: " + str(self.model_manager.getCountTargetList()))

        # Connect every button in main menu with respective function (e.g. hardenTargetMenuBtn when clicked will trigger function goToHardenTargetMenu)
        self.view.targetListMenuBtn.clicked.connect(self.goToTargetListMenu)
        self.view.hardenTargetMenuBtn.clicked.connect(self.goToHardenTargetMenu)
        self.view.patchTargetMenuBtn.clicked.connect(self.goToPatchTargetMenu)

        # Receive signal to update total target counter when changes occur to the target list data
        self.model_manager.targetListUpdated.connect(self.updateTotalTargetCounter)

    # Function to go to the target list menu from main menu
    def goToTargetListMenu(self):
        self.main_window.switchToTargetListMenu()

    # Function to go to the harden target menu from main menu
    def goToHardenTargetMenu(self):
        if self.isEmptyList():
            addWarningMsgBox(
                self.main_window,
                self.errorTitle,
                self.errorMsg
            )
        else:
            self.main_window.switchToHardenTargetMenu()

    # Function to go to the patch target menu from main menu
    def goToPatchTargetMenu(self):
        if self.isEmptyList():
            addWarningMsgBox(
                self.main_window,
                self.errorTitle,
                self.errorMsg
            )
        else:
            self.main_window.switchToPatchTargetMenu()

    # Function to update total target counter in main menu
    def updateTotalTargetCounter(self):
        self.view.totalTargetLbl.setText(f"Total Target: {self.model_manager.getCountTargetList()}")

    # Function to validate empty list
    def isEmptyList(self):
        return True if self.model_manager.getCountTargetList() == 0 else False