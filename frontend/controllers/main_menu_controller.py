from views.main_menu_view import MainMenuView
from models.target_model import TargetModel

class MainMenuController:
    def __init__(self, view:MainMenuView, model:TargetModel, main_window):
        self.view = view
        self.model = model
        self.main_window = main_window

        self.view.totalTargetLbl.setText("Total Target: " + str(self.model.getCountTargetList()))

        self.view.hardenTargetMenuBtn.clicked.connect(self.goToHardenTargetMenu)
        self.view.patchTargetMenuBtn.clicked.connect(self.goToPatchTargetMenu)
        self.view.targetListMenuBtn.clicked.connect(self.goToTargetListMenu)

        # self.model.targetListUpdated.connect(self.updateTotalTargetCounter)

    def goToHardenTargetMenu(self):
        self.main_window.switchToHardenTargetMenu()

    def goToPatchTargetMenu(self):
        self.main_window.switchToPatchTargetMenu()
        # print(f"{self.model.getCountTargetList()}")

    def goToTargetListMenu(self):
        self.main_window.switchToTargetListMenu()

    def updateTotalTargetCounter(self):
        self.view.totalTargetLbl.setText(f"Total Target: {self.model.getCountTargetList()}")