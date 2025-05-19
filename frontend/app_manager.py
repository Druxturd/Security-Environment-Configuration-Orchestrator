from models.target_data_manager import TargetDataManager
from models.package_data_manager import PackageDataManager

from views.main_window_view import MainWindow
from views.main_menu_view import MainMenuView
from views.target_list_menu_view import TargetListMenuView
from views.harden_target_menu_view import HardenTargetMenuView
from views.patch_target_menu_view import PatchTargetMenuView

from controllers.main_menu_controller import MainMenuController
from controllers.target_list_menu_controller import TargetListMenuController
from controllers.harden_target_menu_controller import HardenTargetMenuController
from controllers.patch_target_menu_controller import PatchTargetMenuController

from pages import Page

class AppManager():
    def __init__(self):
        self.init_main_window()
        self.init_model_managers()
        self.init_views()
        self.init_controllers()

        self.config_stacked_widget()
    
    def init_main_window(self):
        self.main_window = MainWindow()
        self.main_window.setWindowTitle("SECOR")
   
    def init_model_managers(self):
        self.model_manager = TargetDataManager()

    def init_views(self):
        self.main_menu_view = MainMenuView()
        self.target_list_menu_view = TargetListMenuView()
        self.harden_target_menu_view = HardenTargetMenuView()
        self.patch_target_menu_view = PatchTargetMenuView()

    def init_controllers(self):
        self.main_menu_controller = MainMenuController(self.main_menu_view, self.model_manager, self.main_window)
        self.target_list_menu_controller = TargetListMenuController(self.target_list_menu_view, self.model_manager, self.main_window)
        self.harden_target_menu_controller = HardenTargetMenuController(self.harden_target_menu_view, self.model_manager, self.main_window)
        self.patch_target_menu_controller = PatchTargetMenuController(self.patch_target_menu_view, self.model_manager, self.main_window)

    def config_stacked_widget(self):
        self.main_window.stacked_widget.insertWidget(Page.MAIN_MENU, self.main_menu_view)
        self.main_window.stacked_widget.insertWidget(Page.TARGET_LIST_MENU, self.target_list_menu_view)
        self.main_window.stacked_widget.insertWidget(Page.HARDEN_TARGET_MENU, self.harden_target_menu_view)
        self.main_window.stacked_widget.insertWidget(Page.PATCH_TARGET_MENU, self.patch_target_menu_view)

        self.main_window.setCentralWidget(self.main_window.stacked_widget)

        # self.main_window.switch_to_main_menu()
        self.main_window.switch_to_target_list_menu()