from models.target_model import TargetModel
from views.harden_target_menu_view import HardenTargetMenuView

class HardenTargetMenuController:
    def __init__(self, view:HardenTargetMenuView, model:TargetModel, main_window):
        self.view = view
        self.model = model
        self.main_window = main_window
        
        self.view.backBtn.clicked.connect(self.goToMainMenu)

    def goToMainMenu(self):
        self.main_window.switchToMainMenu()