import json
import os

from dotenv import load_dotenv
from models.target_data_manager import TargetDataManager
from qasync import asyncSlot
from utils.backend_util import execute_harden
from utils.harden_files import fetch_all_harden_controls
from views.harden_target_menu_view import HardenTargetMenuView
from views.main_window_view import MainWindow

from PySide6.QtCore import QObject, Qt
from PySide6.QtWidgets import QCheckBox, QMessageBox

load_dotenv()
HARDEN_LIST_URL = f"{os.getenv('BACKEND_URL')}/harden"
EXECUTE_SELECTED_HARDEN_URL = f"{HARDEN_LIST_URL}/execute"
EXECUTE_AUTO_HARDEN_URL = f"{HARDEN_LIST_URL}/auto-execute"


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

        self.view.check_btn.clicked.connect(self.check_data)  # temporary

        self.update_total_target_counter()

        self.model_manager.target_list_updated.connect(self.update_total_target_counter)

        # self.fetch_files()
        self.fetch_harden_list()

    ### temporary function
    def check_data(self):
        payload = {
            "controls": [
                cb.property("data") for cb in self.view.check_boxes if cb.isChecked()
            ],
            "targets": self.model_manager.get_payload(),
        }
        print(json.dumps(payload))

    ###

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

    """
    def fetch_files(self):
        try:
            resp = httpx.get(HARDEN_LIST_URL)
            if resp.status_code == 200:
                data = resp.json()
                data_list = data.get("harden_list", [])
                data_list.sort()
                for playbook in data_list:
                    self.check_box = QCheckBox(playbook)
                    self.view.check_boxes.append(self.check_box)
                    self.view.scroll_content_layout.addWidget(self.check_box)

                # Dynamically adjust the height of scrollable content
                self.view.scroll_content.setFixedHeight(len(self.view.check_boxes) * 25)

                # Refresh the UI
                self.view.scroll_content.adjustSize()
                self.view.scroll_area.update()
                self.view.repaint()

        except httpx.RequestError as e:
            print(e)
    """

    @asyncSlot()
    async def execute_selected_harden(self):
        # payload = {
        #     "playbooks": [cb.text() for cb in self.view.check_boxes if cb.isChecked()],
        #     "targets": self.model_manager.get_payload(),
        # }

        # if len(payload["playbooks"]) == 0:
        #     QMessageBox.information(
        #         self.main_window, "Playbook", "Please select minimal 1 playbook"
        #     )

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
        payload = json.dumps(self.model_manager.get_payload())
        self.view.auto_harden_btn.setEnabled(False)

        await execute_harden(self.main_window, EXECUTE_AUTO_HARDEN_URL, payload)

        self.view.auto_harden_btn.setEnabled(True)

    def uncheck_all_selected_items(self):
        for cb in self.view.check_boxes:
            if cb.isChecked():
                cb.setCheckState(Qt.CheckState.Unchecked)
