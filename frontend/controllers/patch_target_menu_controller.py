from PySide6.QtCore import QObject

from views.patch_target_menu_view import PatchTargetMenuView
from views.main_window_view import MainWindow

from models.target_data_manager import TargetDataManager

class PatchTargetMenuController(QObject):
    def __init__(self, view: PatchTargetMenuView, model_manager: TargetDataManager, main_window: MainWindow):
        super().__init__()
        
        self.view = view
        self.model_manager = model_manager
        self.main_window = main_window

        self.view.back_btn.clicked.connect(self.go_to_main_menu)

        self.update_total_target_counter()

        self.model_manager.target_list_updated.connect(self.update_total_target_counter)
        
    def go_to_main_menu(self):
        self.main_window.switch_to_main_menu()

    def update_total_target_counter(self):
        self.view.total_target_lbl.setText(f"Total Target(s): {self.model_manager.get_count_target_list()}")