from models.target_model import TargetModel
from views.patch_target_menu_view import PatchTargetMenuView

class PatchTargetMenuController:
    def __init__(self, view:PatchTargetMenuView, model:TargetModel, main_window):
        self.view = view
        self.model = model
        self.main_window = main_window
        
        self.view.backBtn.clicked.connect(self.goToMainMenu)

    def goToMainMenu(self):
        self.main_window.switchToMainMenu()