from models.target_model import TargetModel
from views.target_list_menu_view import TargetListMenuView

class TargetListMenuController:
    def __init__(self, view:TargetListMenuView, model:TargetModel, main_window):
        self.view = view
        self.model = model
        self.main_window = main_window
        
        self.view.backBtn.clicked.connect(self.goToMainMenu)

    def goToMainMenu(self):
        self.main_window.switchToMainMenu()