import os
from PySide6.QtCore import QObject
from PySide6.QtWidgets import (
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QHBoxLayout,
    QComboBox,
    QLayout
)
from dotenv import load_dotenv
import httpx

from views.patch_target_menu_view import PatchTargetMenuView
from views.main_window_view import MainWindow
from views.select_target_view import SelectTargetView

from controllers.select_target_controller import SelectTargetController

from models.target_data_manager import TargetDataManager

from patch_files import *

load_dotenv()
PATCH_LIST_URL = f"{os.getenv("BACKEND_URL")}/patch"
ALL_HOST_PATCH_LIST_URL = f"{PATCH_LIST_URL}/all-host"
SPECIFIC_HOST_PATCH_LIST_URL = f"{PATCH_LIST_URL}/specific-host"

class PatchTargetMenuController(QObject):
    def __init__(self, view: PatchTargetMenuView, model_manager: TargetDataManager, main_window: MainWindow):
        super().__init__()
        
        self.view = view
        self.model_manager = model_manager
        self.main_window = main_window

        self.view.back_btn.clicked.connect(self.go_to_main_menu)
        self.view.all_playbook_combo_box.currentIndexChanged.connect(self.all_combo_box_on_index_changed)
        self.view.specific_playbook_combo_box.currentIndexChanged.connect(self.specific_combo_box_on_index_changed)
        self.view.select_target_btn.clicked.connect(self.display_select_target_view)
        self.update_total_target_counter()
        self.update_selected_target_counter()

        self.model_manager.target_list_updated.connect(self.update_total_target_counter)

        self.fetch_patch_files()
        
    def go_to_main_menu(self):
        self.main_window.switch_to_main_menu()

    def update_total_target_counter(self):
        self.view.total_target_lbl.setText(f"Total Target(s): {self.model_manager.get_count_target_list()}")

    def update_selected_target_counter(self):
        self.view.total_selected_target_lbl.setText(f"Total Selected Target(s): {self.model_manager.get_count_checked_target()}")

    def fetch_patch_files(self):
        self.fetch_all_host_patch_files()
        self.fetch_specific_host_patch_files()

    def fetch_all_host_patch_files(self):
        try:
            resp = httpx.get(ALL_HOST_PATCH_LIST_URL)
            if resp.status_code == 200:
                data = resp.json()
                data_list = data.get("patch_list", [])
                data_list.sort()
                for i, playbook in enumerate(data_list):
                    self.view.all_playbook_combo_box.insertItem(i, playbook, str(playbook))

        except httpx.RequestError as e:
            print(e)
        
    def fetch_specific_host_patch_files(self):
        try:
            resp = httpx.get(SPECIFIC_HOST_PATCH_LIST_URL)
            if resp.status_code == 200:
                data = resp.json()
                data_list = data.get("patch_list", [])
                data_list.sort()
                for i, playbook in enumerate(data_list):
                    self.view.specific_playbook_combo_box.insertItem(i, playbook, str(playbook))

        except httpx.RequestError as e:
            print(e)

    def all_combo_box_on_index_changed(self):
        all_combo_box = self.view.all_playbook_combo_box
        self.update_detail_all_patch(all_combo_box.currentData())
        
    def specific_combo_box_on_index_changed(self):
        specific_combo_box = self.view.specific_playbook_combo_box
        self.update_detail_specific_patch(specific_combo_box.currentData())

    def clear_layout(self, layout: QLayout):
        while layout.count():
            item = layout.takeAt(0)

            widget = item.widget()
            if widget is not None:
                widget.setParent(None)

            child_layout = item.layout()
            if child_layout is not None:
                self.clear_layout(child_layout)
                del child_layout

    def update_detail_all_patch(self, data):
        layout = self.view.all_detail_widget_layout

        self.clear_layout(layout)

        if data == PATCH_ALL_HOST.MANAGE_SERVICES:
            services_layout = QVBoxLayout()
            services_lbl = QLabel("Services (use comma (,) for multiple services):")
            services_inp = QLineEdit()
            services_layout.addWidget(services_lbl)
            services_layout.addWidget(services_inp)

            action_layout = QHBoxLayout()
            action_lbl = QLabel("Action:")
            action_lbl.setFixedWidth(action_lbl.sizeHint().width())
            action_combo_box = QComboBox()
            action_combo_box.insertItem(0, "Stop Service(s)", "stopped")
            action_combo_box.insertItem(1, "Start Service(s)", "started")
            action_layout.addWidget(action_lbl)
            action_layout.addWidget(action_combo_box)

            layout.addLayout(services_layout)
            layout.addLayout(action_layout)

        elif data == PATCH_ALL_HOST.UPDATE_PORT:

            ports_layout = QVBoxLayout()
            ports_lbl = QLabel("Ports (user comma (,) for multiple ports)")
            ports_inp = QLineEdit()
            ports_layout.addWidget(ports_lbl)
            ports_layout.addWidget(ports_inp)

            layout.addLayout(ports_layout)
            

    def update_detail_specific_patch(self, data):
        layout = self.view.specific_detail_widget_layout

        self.clear_layout(layout)

        if data == PATCH_SPECIFIC_HOST.UPDATER_LATEST:
            packages_to_update_layout = QVBoxLayout()
            packages_to_update_lbl = QLabel("Package(s) to update (use comma (,) for multiple packages):")
            packages_to_update_inp = QLineEdit()
            packages_to_update_layout.addWidget(packages_to_update_lbl)
            packages_to_update_layout.addWidget(packages_to_update_inp)

            layout.addLayout(packages_to_update_layout)
    
    def display_select_target_view(self):
        select_target_view = SelectTargetView()
        select_target_controller = SelectTargetController(select_target_view, self.model_manager, self)
        select_target_view.adjustSize()
        select_target_view.exec()