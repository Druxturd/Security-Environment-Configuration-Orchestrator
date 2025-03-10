from models.target_model import TargetModel
from views.patch_target_menu_view import PatchTargetMenuView

class PatchTargetMenuController:
    def __init__(self, view:PatchTargetMenuView, model:TargetModel, main_window):
        # Store the view, model, main window that being passed into the controller
        self.view = view
        self.model = model
        self.main_window = main_window

        # Set the initial total target counter
        self.view.totalTargetLbl.setText(f"Total Target: {self.model.getCountTargetList()}")
        
        # Connect every button in harden target menu with respective function (e.g. backBtn when clicked will trigger function goToMainMenu)
        self.view.backBtn.clicked.connect(self.goToMainMenu)

        # Receive signal to update total target counter when changes occur to the target list data
        self.model.targetListUpdated.connect(self.updateTotalTargetCounter)

    # Function to go to the main menu from patch target menu
    def goToMainMenu(self):
        self.main_window.switchToMainMenu()
    
    # Function to update total target counter in main menu
    def updateTotalTargetCounter(self):
        self.view.totalTargetLbl.setText("Total Target: " + str(self.model.getCountTargetList()))