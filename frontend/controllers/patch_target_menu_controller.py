from models.target_data_manager import TargetDataManager
from views.patch_target_menu_view import PatchTargetMenuView
from views.main_window_view import MainWindow

class PatchTargetMenuController:
    def __init__(self, view:PatchTargetMenuView, model_manager: TargetDataManager, main_window:MainWindow):
        # Store the view, model manager, main window that being passed into the controller
        self.view = view
        self.model_manager = model_manager
        self.main_window = main_window

        # Set the initial total target counter
        self.view.totalTargetLbl.setText(f"Total Target: {self.model_manager.getCountTargetList()}")
        
        # Connect every button in harden target menu with respective function (e.g. backBtn when clicked will trigger function goToMainMenu)
        self.view.backBtn.clicked.connect(self.goToMainMenu)

        # Receive signal to update total target counter when changes occur to the target list data
        self.model_manager.targetListUpdated.connect(self.updateTotalTargetCounter)

    # Function to go to the main menu from patch target menu
    def goToMainMenu(self):
        self.main_window.switchToMainMenu()
    
    # Function to update total target counter in main menu
    def updateTotalTargetCounter(self):
        self.view.totalTargetLbl.setText("Total Target: " + str(self.model_manager.getCountTargetList()))