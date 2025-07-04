import os

from dotenv import load_dotenv
from models.target_data_manager import TargetDataManager
from qasync import asyncSlot
from utils.backend_util import execute_harden
from utils.harden_files import SEMI_HARDEN_CONTROL, fetch_all_harden_controls
from views.harden_target_menu_view import HardenTargetMenuView
from views.main_window_view import MainWindow

from PySide6.QtCore import QObject, Qt
from PySide6.QtWidgets import QCheckBox, QMessageBox

load_dotenv()
HARDEN_LIST_URL = f"{os.getenv('BACKEND_URL')}/harden"
EXECUTE_SELECTED_HARDEN_URL = f"{HARDEN_LIST_URL}/execute"
EXECUTE_AUTO_HARDEN_URL = f"{HARDEN_LIST_URL}/auto-execute"
EXECUTE_SEMI_AUTO_HARDEN_URL = f"{HARDEN_LIST_URL}/semi-auto-execute"


class HardenTargetMenuController(QObject):
    def __init__(
        self,
        view: HardenTargetMenuView,
        model_manager: TargetDataManager,
        main_window: MainWindow,
    ):
        super().__init__()

        self.view = view
        self.model_manager = model_manager
        self.main_window = main_window

        self.view.back_btn.clicked.connect(self.go_to_main_menu)

        self.view.execute_harden_btn.clicked.connect(self.execute_selected_harden)

        self.view.auto_harden_btn.clicked.connect(self.execute_auto_harden)

        self.view.semi_harden_btn.clicked.connect(self.execute_semi_auto_harden)

        self.update_total_target_counter()

        self.model_manager.target_list_updated.connect(self.update_total_target_counter)

        self.fetch_harden_list()

    def go_to_main_menu(self):
        self.main_window.switch_to_main_menu()

    def update_total_target_counter(self):
        self.view.total_target_list_lbl.setText(
            f"Total Target(s): {self.model_manager.get_count_target_list()}"
        )

    def fetch_harden_list(self):
        harden_list = fetch_all_harden_controls()
        for data in harden_list:
            self.check_box = QCheckBox(data.value["name"])
            self.check_box.setProperty("data", data.value)
            self.view.check_boxes.append(self.check_box)
            self.view.scroll_content_layout.addWidget(self.check_box)

        self.view.scroll_content.setFixedHeight(len(self.view.check_boxes) * 25)

        self.view.scroll_content.adjustSize()
        self.view.scroll_area.update()
        self.view.repaint()

    @asyncSlot()
    async def execute_selected_harden(self):
        payload = {
            "controls": [
                cb.property("data") for cb in self.view.check_boxes if cb.isChecked()
            ],
            "targets": self.model_manager.get_payload(),
        }
        if len(payload["controls"]) == 0:
            QMessageBox.information(
                self.main_window, "Controls", "Please select minimal 1 harden control"
            )
        else:
            self.view.execute_harden_btn.setEnabled(False)

            await execute_harden(self.main_window, EXECUTE_SELECTED_HARDEN_URL, payload)

            self.uncheck_all_selected_items()
            self.view.execute_harden_btn.setEnabled(True)

    @asyncSlot()
    async def execute_auto_harden(self):
        payload = {"targets": self.model_manager.get_payload()}
        self.view.auto_harden_btn.setEnabled(False)

        await execute_harden(self.main_window, EXECUTE_AUTO_HARDEN_URL, payload)

        self.view.auto_harden_btn.setEnabled(True)

    @asyncSlot()
    async def execute_semi_auto_harden(self):
        payload = {
            "targets": self.model_manager.get_payload(),
            "controls": SEMI_HARDEN_CONTROL.CONTROLS.value,
        }
        self.view.semi_harden_btn.setEnabled(False)

        await execute_harden(self.main_window, EXECUTE_SEMI_AUTO_HARDEN_URL, payload)

        self.view.semi_harden_btn.setEnabled(True)

    def uncheck_all_selected_items(self):
        for cb in self.view.check_boxes:
            if cb.isChecked():
                cb.setCheckState(Qt.CheckState.Unchecked)
