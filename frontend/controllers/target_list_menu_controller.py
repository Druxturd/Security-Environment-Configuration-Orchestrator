from datetime import datetime
import math
from pathlib import Path
from PySide6.QtCore import QObject
from PySide6.QtWidgets import QFileDialog, QMessageBox
import httpx
import pandas as pd

from views.target_list_menu_view import TargetListMenuView
from views.main_window_view import MainWindow

from models.target_data_manager import TargetDataManager
from models.target_model import TargetModel

from dotenv import load_dotenv
import os

load_dotenv()
TEMPLATE_URL = f"{os.getenv("BACKEND_URL")}/download-template"

class TargetListMenuController(QObject):
    def __init__(self, view: TargetListMenuView, model_manager: TargetDataManager, main_window: MainWindow):
        super().__init__()

        self.view = view
        self.model_manager = model_manager
        self.main_window = main_window

        self.input_error = "Input Error"
        self.error_msg = [
            "IP Address must be fill!",
            "Host name must be fill!",
            "SSH Key must be fill"
        ]

        self.view.back_btn.clicked.connect(self.go_to_main_menu)
        self.view.download_template_btn.clicked.connect(self.download_template)
        self.view.upload_excel_btn.clicked.connect(self.upload_excel_file)
        self.view.add_target_btn.clicked.connect(self.add_target)
        self.view.clear_target_btn.clicked.connect(self.clear_target_list)

        self.update_total_target_counter()

        self.model_manager.target_list_updated.connect(self.update_total_target_counter)

    def go_to_main_menu(self):
        self.main_window.switch_to_main_menu()

    def update_total_target_counter(self):
        self.view.total_target_lbl.setText(f"Total Target(s): {self.model_manager.get_count_target_list()}")

    def download_template(self):
        try:
            resp = httpx.get(TEMPLATE_URL)

            if resp.status_code == 404:
                print("error download template")
                return

            resp.raise_for_status() # Raises HTTPError for 4xx/5xx

            downloads_folder = Path.home() / "Downloads"
            time_stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"template_{time_stamp}.xlsx"
            file_path = downloads_folder / file_name

            with open(file_path, "wb") as f:
                f.write(resp.content)

            QMessageBox.information(self.main_window, "Download Successful", f"The template has been downloaded to:\n{file_path}")
        
        except httpx.TimeoutException:
            print("timeout")
        except httpx.ConnectError:
            print("connection error")
        except httpx.HTTPError as http_err:
            print(http_err)
        except Exception as e:
            print(e)

    def upload_excel_file(self):
        options = QFileDialog().options()
        file_path, _ = QFileDialog.getOpenFileName(
            self.main_window,
            "Open Excel File",
            "",
            "Excel Files (*.xlsx *.xls)",
            options=options
        )

        if not file_path: # if user cancel upload
            return
        
        try:
            new_target_added = 0

            df = pd.read_excel(file_path, engine='openpyxl')

            required_columns = {"IP Address", "Host Name", "SSH Private Key", "OS Version Name"}

            # Validate header
            if not required_columns.issubset(df.columns):
                raise ValueError(f"Missing required column(s): {required_columns - set(df.columns)}")

            for i, row in df.iterrows():
                try:
                    _ip = str(row['IP Address']).strip()
                    _host = str(row['Host Name']).strip()
                    _user = str(row['SSH Username']).strip()
                    _p = str(row['SSH Port']).strip()
                    _port = "22" if math.isnan(float(_p)) else str(int(float(_p)))
                    _key = str(row['SSH Private Key']).strip()
                    _os = str(row['OS Version Name']).strip()

                    if not _ip or not _host or not _user or not _port or not _key or not _os:
                        raise ValueError("Empty value in required column(s)")
                    
                    _filtered_os = _os.lower().split()

                    _osName = _filtered_os[0]
                    _osVersion = _filtered_os[1]

                    if _osName in TargetDataManager.supported_os_version and any(_osVersion.startswith(x) for x in TargetDataManager.supported_os_version[_osName]):
                        target = TargetModel(ip_address=_ip, host_name=_host, ssh_username=_user, ssh_port=_port, ssh_private_key=_key, os_version_name=_os)
                    else:
                        continue

                    if self.model_manager.add_new_target(target):
                        new_target_added += 1
            
                except Exception as e:
                    QMessageBox.warning(self.view, "Row Error", f"Skipping row {i+2}: {str(e)}") # type: ignore
        
            QMessageBox.information(self.main_window, "Upload Successful", f"Added {new_target_added} new target(s).\nTotal target(s): {self.model_manager.get_count_target_list()}")

            self.update_total_target_counter()
        
        except Exception as e:
            QMessageBox.critical(self.main_window, "Error", f"Failed to read Excel file:\n{str(e)}")
    
    def add_target(self):
        ip_address = self.view.ip_input.text().strip()
        host_name = self.view.host_input.text().strip()
        key = self.view.key_input.toPlainText().strip()

        if not ip_address:
            QMessageBox.warning(self.main_window, self.input_error, self.error_msg[0])
            return
        
        elif not host_name:
            QMessageBox.warning(self.main_window, self.input_error, self.error_msg[1])
            return
        
        elif not key:
            QMessageBox.warning(self.main_window, self.input_error, self.error_msg[2])
            return
        
        newTarget = TargetModel(ip_address, host_name, key)

        if self.model_manager.add_new_target(newTarget):
            self.update_total_target_counter()
            QMessageBox.information(
                self.main_window,
                "Add New Target Successful",
                f"Added new target.\nTotal target list: {self.model_manager.get_count_target_list()}"
            )
        else:
            QMessageBox.information(
                self.main_window,
                "Add New Target Failed",
                f"Duplicated target list!"
            )
        
        self.clear_input()

    def clear_input(self):
        self.view.ip_input.clear()
        self.view.host_input.clear()
        self.view.key_input.clear()
    
    def clear_target_list(self):
        self.model_manager.clear_target_list()
        QMessageBox.information(
            self.main_window,
            "Clear Target Successful",
            "Target list has been cleared"
        )