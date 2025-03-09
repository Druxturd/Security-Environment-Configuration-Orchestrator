from models.target_model import TargetModel
from views.target_list_menu_view import TargetListMenuView

class TargetListMenuController:
    def __init__(self, view:TargetListMenuView, model:TargetModel, main_window):
        self.view = view
        self.model = model
        self.main_window = main_window

        self.view.totalTargetLbl.setText("Total Target: " + str(self.model.getCountTargetList()))

        self.view.addTargetBtn.clicked.connect(self.addTarget)
        
        self.view.backBtn.clicked.connect(self.goToMainMenu)

        # self.model.targetListUpdated.connect(self.updateTotalTargetCounter)

    def goToMainMenu(self):
        self.main_window.switchToMainMenu()
        # self.main_window.updateTotalTargetCounter()

    def updateTotalTargetCounter(self):
        self.view.totalTargetLbl.setText("Total Target: " + str(self.model.getCountTargetList()))

    # Temp function to add counter
    def addTarget(self):
        self.model.addCounter()
        self.updateTotalTargetCounter()