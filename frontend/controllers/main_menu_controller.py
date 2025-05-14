from views.main_menu_view import MainMenuView
from views.main_window_view import MainWindow

from models.target_data_manager import TargetDataManager

from utils.message_box_util import *

class MainMenuController:
    def __init__(self, view: MainMenuView, model_manager: TargetDataManager, main_window: MainWindow):
        self.view = view
        self.model_manager = model_manager
        self.main_window = main_window

        self.error_title = "Error"
        self.error_msg = "Empty List!"

        self.view.target_list_menu_btn.clicked.connect(self.go_to_target_list_menu)
        self.view.harden_target_menu_btn.clicked.connect(self.go_to_harden_target_menu)
        self.view.patch_target_menu_btn.clicked.connect(self.go_to_patch_target_menu)

        self.update_total_target_counter()

        self.model_manager.target_list_updated.connect(self.update_total_target_counter)

    def go_to_target_list_menu(self):
        self.main_window.switch_to_target_list_menu()

    def go_to_harden_target_menu(self):
        if self.is_empty_list():
            add_warning_msg_box(
                self.main_window,
                self.error_title,
                self.error_msg
            )
        else:
            self.main_window.switch_to_harden_target_menu()
    
    def go_to_patch_target_menu(self):
        if self.is_empty_list():
            add_warning_msg_box(
                self.main_window,
                self.error_title,
                self.error_msg
            )
        else:
            self.main_window.switch_to_patch_target_menu()

    def update_total_target_counter(self):
        self.view.total_target_lbl.setText(f"Total Target(s): {self.model_manager.get_count_target_list()}")

    def is_empty_list(self):
        return False
        # return True if self.model_manager.get_count_target_list() == 0 else False