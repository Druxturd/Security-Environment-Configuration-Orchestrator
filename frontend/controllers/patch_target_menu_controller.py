import os

import httpx
from dotenv import load_dotenv
from qasync import asyncSlot

from frontend.models.target_data_manager import TargetDataManager
from frontend.utils.backend_util import execute_patch
from frontend.utils.patch_files import PATCH_TYPE
from frontend.views.main_window_view import MainWindow
from frontend.views.patch_target_menu_view import PatchTargetMenuView
from PySide6.QtCore import QObject
from PySide6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QLabel,
    QLayout,
    QLineEdit,
    QMessageBox,
    QVBoxLayout,
)

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
PATCH_LIST_URL = f"{os.getenv('BACKEND_URL')}/patch"
EXECUTE_PATCH_URL = f"{PATCH_LIST_URL}/execute"


class PatchTargetMenuController(QObject):
    def __init__(
        self,
        view: PatchTargetMenuView,
        model_manager: TargetDataManager,
        main_window: MainWindow,
    ):
        super().__init__()

        self.view = view
        self.model_manager = model_manager
        self.main_window = main_window

        self.view.back_btn.clicked.connect(self.go_to_main_menu)
        self.view.execute_patch_btn.clicked.connect(self.execute_selected_patch)

        self.view.playbook_combo_box.currentIndexChanged.connect(
            self.combo_box_on_index_changed
        )
        self.update_total_target_counter()

        self.model_manager.target_list_updated.connect(self.update_total_target_counter)

        self.fetch_all_patch_files()

    def go_to_main_menu(self):
        self.main_window.switch_to_main_menu()

    def update_total_target_counter(self):
        self.view.total_target_lbl.setText(
            f"Total Target(s): {self.model_manager.get_count_target_list()}"
        )

    def fetch_all_patch_files(self):
        try:
            resp = httpx.get(PATCH_LIST_URL)
            if resp.status_code == 200:
                data = resp.json()
                data_list = data.get("patch_list", [])
                data_list.sort()
                for i, playbook in enumerate(data_list):
                    self.view.playbook_combo_box.insertItem(i, playbook, str(playbook))

        except httpx.RequestError as e:
            print(e)

    def combo_box_on_index_changed(self):
        combo_box = self.view.playbook_combo_box
        self.update_detail_all_patch(combo_box.currentData())

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
        layout = self.view.detail_widget_layout

        self.clear_layout(layout)

        if data == PATCH_TYPE.CLOSE_PORT:
            self.close_ports_layout = QVBoxLayout()
            self.close_ports_header = QLabel(
                "Please input the desired port(s) you want to close!"
            )
            self.close_ports_lbl = QLabel("Ports (user comma (,) for multiple ports):")
            self.close_ports_inp = QLineEdit()
            self.close_ports_layout.addWidget(self.close_ports_header)
            self.close_ports_layout.addWidget(self.close_ports_lbl)
            self.close_ports_layout.addWidget(self.close_ports_inp)

            layout.addLayout(self.close_ports_layout)

        elif data == PATCH_TYPE.MANAGE_SERVICES:
            self.services_layout = QVBoxLayout()
            self.services_header = QLabel(
                "Please input the desired service(s) you want to start/stop!"
            )
            self.services_lbl = QLabel(
                "Services (use comma (,) for multiple services):"
            )
            self.services_inp = QLineEdit()
            self.services_layout.addWidget(self.services_header)
            self.services_layout.addWidget(self.services_lbl)
            self.services_layout.addWidget(self.services_inp)

            self.action_layout = QHBoxLayout()
            self.action_lbl = QLabel("Action:")
            self.action_lbl.setFixedWidth(self.action_lbl.sizeHint().width())
            self.action_combo_box = QComboBox()
            self.action_combo_box.insertItem(0, "Stop Service(s)", "stopped")
            self.action_combo_box.insertItem(1, "Start Service(s)", "started")
            self.action_layout.addWidget(self.action_lbl)
            self.action_layout.addWidget(self.action_combo_box)

            layout.addLayout(self.services_layout)
            layout.addLayout(self.action_layout)

        elif data == PATCH_TYPE.OPEN_PORT:
            self.open_ports_layout = QVBoxLayout()
            self.open_ports_header = QLabel(
                "Please input the desired port(s) you want to open!"
            )
            self.open_ports_lbl = QLabel("Ports (user comma (,) for multiple ports):")
            self.open_ports_inp = QLineEdit()
            self.open_ports_layout.addWidget(self.open_ports_header)
            self.open_ports_layout.addWidget(self.open_ports_lbl)
            self.open_ports_layout.addWidget(self.open_ports_inp)

            layout.addLayout(self.open_ports_layout)

        elif data == PATCH_TYPE.UPDATE_INSTALL:
            self.update_layout = QVBoxLayout()
            self.update_header = QLabel(
                "Please input the desired package(s) to install or update!\nFor example: mysql-server"
            )
            self.update_lbl = QLabel(
                "Package(s) to install or update to the latest version (use comma (,) for multiple services):"
            )
            self.update_inp = QLineEdit()
            self.update_layout.addWidget(self.update_header)
            self.update_layout.addWidget(self.update_lbl)
            self.update_layout.addWidget(self.update_inp)

            layout.addLayout(self.update_layout)

        self.view.adjustSize()

    @asyncSlot()
    async def execute_selected_patch(self):
        data = self.view.playbook_combo_box.currentData()

        if data == PATCH_TYPE.CLOSE_PORT:
            port_inp = self.close_ports_inp.text().strip()
            ports = []
            invalid_ports = []
            for x in port_inp.split(","):
                if x.strip().isnumeric():
                    ports.append(x.strip())
                else:
                    invalid_ports.append(x.strip())

            if invalid_ports:
                QMessageBox.warning(
                    self.main_window, "Warning", f"Invalid Input:\n{invalid_ports}"
                )
                return

            payload = {
                "playbook": str(data.strip()),
                "extra_vars": {"ports": ports},
                "targets": self.model_manager.get_payload(),
            }

            self.view.execute_patch_btn.setEnabled(False)

            await execute_patch(self.main_window, EXECUTE_PATCH_URL, payload)

            self.view.execute_patch_btn.setEnabled(True)

        elif data == PATCH_TYPE.MANAGE_SERVICES:
            service_inp = self.services_inp.text().strip()
            services = []
            invalid_services = []
            for x in service_inp.split(","):
                if x.strip():
                    services.append(x.strip())
                else:
                    invalid_services.append(x.strip())

            if invalid_services:
                QMessageBox.warning(
                    self.main_window, "Warning", f"Invalid Input:\n{invalid_services}"
                )
                return

            payload = {
                "playbook": str(data.strip()),
                "extra_vars": {
                    "services": services,
                    "action": str(self.action_combo_box.currentData()),
                },
                "targets": self.model_manager.get_payload(),
            }

            self.view.execute_patch_btn.setEnabled(False)

            await execute_patch(self.main_window, EXECUTE_PATCH_URL, payload)

            self.view.execute_patch_btn.setEnabled(True)

        elif data == PATCH_TYPE.OPEN_PORT:
            port_inp = self.open_ports_inp.text().strip()
            ports = []
            invalid_ports = []
            for x in port_inp.split(","):
                if x.strip().isnumeric():
                    ports.append(x.strip())
                else:
                    invalid_ports.append(x.strip())

            if invalid_ports:
                QMessageBox.warning(
                    self.main_window, "Warning", f"Invalid Input:\n{invalid_ports}"
                )
                return

            payload = {
                "playbook": str(data.strip()),
                "extra_vars": {"ports": ports},
                "targets": self.model_manager.get_payload(),
            }

            self.view.execute_patch_btn.setEnabled(False)

            await execute_patch(self.main_window, EXECUTE_PATCH_URL, payload)

            self.view.execute_patch_btn.setEnabled(True)

        elif data == PATCH_TYPE.UPDATE_INSTALL:
            package_inp = self.update_inp.text().strip()
            packages = []
            invalid_packages = []
            for x in package_inp.split(","):
                if x.strip():
                    packages.append(x.strip())
                else:
                    invalid_packages.append(x.strip())

            if invalid_packages:
                QMessageBox.warning(
                    self.main_window, "Warning", f"Invalid Input:\n{invalid_packages}"
                )
                return

            payload = {
                "playbook": str(data.strip()),
                "extra_vars": {"packages_to_update": packages},
                "targets": self.model_manager.get_payload(),
            }

            self.view.execute_patch_btn.setEnabled(False)

            await execute_patch(self.main_window, EXECUTE_PATCH_URL, payload)

            self.view.execute_patch_btn.setEnabled(True)
