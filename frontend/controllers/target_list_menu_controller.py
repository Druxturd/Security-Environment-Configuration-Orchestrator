from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QFileDialog
from qasync import asyncSlot
from models.target_model import TargetModel
from models.target_data_manager import TargetDataManager
from views.target_list_menu_view import TargetListMenuView
from views.main_window_view import MainWindow
from utils.layout_utils import addCriticalMsgBox, addInformationMsgBox, addWarningMsgBox
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime
import asyncio
import os
import requests
import csv

load_dotenv()
TEMPLATE_URL = f"{os.getenv("BACKEND_URL")}/download-template"

### temporary endpoint test ansible runner URL
INSTALL_NGINX_URL = f"{os.getenv("BACKEND_URL")}/install-nginx"
UNINSTALL_NGINX_URL = f"{os.getenv("BACKEND_URL")}/uninstall-nginx"
############

class TargetListMenuController(QObject):
    def __init__(self, view:TargetListMenuView, model_manager:TargetDataManager, main_window:MainWindow):
        super().__init__()
        # Store the view, model, main window that being passed into the controller
        self.view = view
        self.model_manager = model_manager
        self.main_window = main_window

        self.inputError = "Input Error"
        self.errorMsg = [
            "IP Address must be fill!",
            "Host name must be fill!",
            "SSH Key must be fill"
        ]

        # Set the initial total target counter
        self.view.totalTargetLbl.setText(f"Total Target: {self.model_manager.getCountTargetList()}")

        # Connect every button in harden target menu with respective function (e.g. backBtn when clicked will trigger function goToMainMenu)
        self.view.clearTargetBtn.clicked.connect(self.model_manager.clearTargetList)
        self.view.downloadTemplateBtn.clicked.connect(self.downloadTemplate)
        self.view.uploadCSVBtn.clicked.connect(self.uploadCSVFile)
        self.view.addTargetBtn.clicked.connect(self.addTarget)
        self.view.backBtn.clicked.connect(self.goToMainMenu)

        # Receive signal to update total target counter when changes occur to the target list data
        self.model_manager.targetListUpdated.connect(self.updateTotalTargetCounter)

    # Function to go back to main menu from target list menu
    def goToMainMenu(self):
        self.main_window.switchToMainMenu()

    # Function to update total target counter
    def updateTotalTargetCounter(self):
        self.view.totalTargetLbl.setText("Total Target: " + str(self.model_manager.getCountTargetList()))

    # Function to download template.csv
    def downloadTemplate(self):
        try:
            resp = requests.get(TEMPLATE_URL, timeout=10)

            if resp.status_code == 404:
                print("error download template")
                return

            resp.raise_for_status() # Raises HTTPError for 4xx/5xx

            downloads_folder = Path.home() / "Downloads"
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"template_{timestamp}.csv"
            file_path = downloads_folder / filename

            with open(file_path, "wb") as f:
                f.write(resp.content)

            addInformationMsgBox(
                self.main_window,
                "Download Successful",
                f"The template has been downloaded to:\n{file_path}"
            )
        
        except requests.exceptions.Timeout:
            print("timeout")
        except requests.exceptions.ConnectionError:
            print("connection error")
        except requests.exceptions.HTTPError as http_err:
            print(http_err)
        except Exception as e:
            print(e)

    # Function to upload target list csv
    def uploadCSVFile(self):
        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getOpenFileName(
            self.main_window,
            "Open CSV File",
            "",
            "CSV Files (*.csv)",
            options=options
        )

        if not filePath:
            return
        
        try:
            newTargetAdded = 0
            with open(filePath, mode='r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                requiredFields = {"IPAddress", "hostName", "SSHKey"}
                
                # Validate header
                if not requiredFields.issubset(reader.fieldnames):  # type: ignore
                    missing = requiredFields - set(reader.fieldnames or [])
                    raise ValueError(f"Missing required column(s): {', '.join(missing)}")

                for i, row in enumerate(reader, start=2):
                    try:
                        ip = row['IPAddress'].strip()
                        host = row['hostName'].strip()
                        key = row['SSHKey'].strip()

                        if not ip or not host or not key:
                            raise ValueError("One or more required fields are empty")

                        target = TargetModel(IPAddress=ip, hostName=host, SSHKey=key)

                        if self.model_manager.addNewTarget(target):
                            newTargetAdded += 1

                    except Exception as e:
                        addWarningMsgBox(
                            self.main_window,
                            "Row Error",
                            f"Skipping invalid row {i}: {str(e)}"
                        )
                        continue
            
            addInformationMsgBox(
                self.main_window,
                "Upload Successful",
                f"Added {newTargetAdded} new target(s).\nTotal target list: {self.model_manager.getCountTargetList()}"
            )

            self.updateTotalTargetCounter()

        except Exception as e:
            addCriticalMsgBox(
                self.main_window,
                "Error",
                f"Failed to read CSV:\n{str(e)}"
            )

    # Function to add new target
    def addTarget(self):
        IPAddress = self.view.IPAddressInput.text().strip()
        hostName = self.view.hostNameInput.text().strip()
        SSHKey = self.view.SSHKeyInput.toPlainText().strip()

        if not IPAddress:
            addWarningMsgBox(self.main_window, self.inputError, self.errorMsg[0])
            return
        
        elif not hostName:
            addWarningMsgBox(self.main_window, self.inputError, self.errorMsg[1])
            return
        
        elif not SSHKey:
            addWarningMsgBox(self.main_window, self.inputError, self.errorMsg[2])
            return
        
        newTarget = TargetModel(IPAddress, hostName, SSHKey)

        if self.model_manager.addNewTarget(newTarget):
            self.updateTotalTargetCounter()
            addInformationMsgBox(
                self.main_window,
                "Add New Target Successful",
                f"Added new target.\nTotal target list: {self.model_manager.getCountTargetList()}"
            )
        else:
            addInformationMsgBox(
                self.main_window,
                "Add New Target Failed",
                f"Duplicated target list!"
            )
        
        self.clearInput()

    # Function to clear input
    def clearInput(self):
        self.view.IPAddressInput.clear()
        self.view.hostNameInput.clear()
        self.view.SSHKeyInput.clear()