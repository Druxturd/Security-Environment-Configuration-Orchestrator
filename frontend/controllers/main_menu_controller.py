from views.main_menu_view import MainMenuView
from models.target_model import TargetModel

class MainMenuController:
    def __init__(self, view:MainMenuView, model:TargetModel, main_window):
        # Store the view, model, main window that being passed into the controller
        self.view = view
        self.model = model
        self.main_window = main_window

        # Set the initial total target counter
        self.view.totalTargetLbl.setText("Total Target: " + str(self.model.getCountTargetList()))

        # Connect every button in main menu with respective function (e.g. hardenTargetMenuBtn when clicked will trigger function goToHardenTargetMenu)
        self.view.hardenTargetMenuBtn.clicked.connect(self.goToHardenTargetMenu)
        self.view.patchTargetMenuBtn.clicked.connect(self.goToPatchTargetMenu)
        self.view.targetListMenuBtn.clicked.connect(self.goToTargetListMenu)

        # Receive signal to update total target counter when changes occur to the target list data
        self.model.targetListUpdated.connect(self.updateTotalTargetCounter)

    # Function to go to the harden target menu from main menu
    def goToHardenTargetMenu(self):
        self.main_window.switchToHardenTargetMenu()

    # Function to go to the patch target menu from main menu
    def goToPatchTargetMenu(self):
        self.main_window.switchToPatchTargetMenu()

    # Function to go to the target list menu from main menu
    def goToTargetListMenu(self):
        self.main_window.switchToTargetListMenu()

    # Function to update total target counter in main menu
    def updateTotalTargetCounter(self):
        self.view.totalTargetLbl.setText(f"Total Target: {self.model.getCountTargetList()}")