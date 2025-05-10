import math
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QFileDialog
from models.target_model import TargetModel
from models.target_data_manager import TargetDataManager
from views.target_list_menu_view import TargetListMenuView
from views.main_window_view import MainWindow
from utils.message_box_util import addCriticalMsgBox, addInformationMsgBox, addWarningMsgBox
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime
import pandas as pd
import os
import requests

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
        self.view.uploadBtn.clicked.connect(self.uploadExcelFile)
        self.view.addTargetBtn.clicked.connect(self.addTarget)
        self.view.backBtn.clicked.connect(self.goToMainMenu)

        ### temporary btn
        self.view.checkBtn.clicked.connect(self.checkData)
        ###

        # Receive signal to update total target counter when changes occur to the target list data
        self.model_manager.targetListUpdated.connect(self.updateTotalTargetCounter)

    def goToMainMenu(self):
        self.main_window.switchToMainMenu()

    def updateTotalTargetCounter(self):
        self.view.totalTargetLbl.setText("Total Target: " + str(self.model_manager.getCountTargetList()))

    def downloadTemplate(self):
        try:
            resp = requests.get(TEMPLATE_URL, timeout=10)

            if resp.status_code == 404:
                print("error download template")
                return

            resp.raise_for_status() # Raises HTTPError for 4xx/5xx

            downloads_folder = Path.home() / "Downloads"
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"template_{timestamp}.xlsx"
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

    ### temporary function
    def checkData(self):
        for x in self.model_manager.getTargetList():
            print(f"ip: {x.IPAddress}")
            print(f"host: {x.hostName}")
            print(f"ssh username: {x.SSHUsername}")
            print(f"key: {x.SSHKey}")
            print(f"port: {x.SSHPort}")
            print(f"os: {x.osVersionName}")
            print("")
    #########
    
    def uploadExcelFile(self):
        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getOpenFileName(
            self.main_window,
            "Open Excel File",
            "",
            "Excel Files (*.xlsx *.xls)",
            options=options
        )

        if not filePath: # if user cancel upload
            return

        try:
            newTargetAdded = 0

            df = pd.read_excel(filePath, engine='openpyxl')

            requiredColumns = {"IP Address", "Host Name", "SSH Private Key", "OS Version Name"}

            # Validate header
            if not requiredColumns.issubset(df.columns):
                raise ValueError(f"Missing required column(s): {requiredColumns - set(df.columns)}")

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
                    
                    _filteredOS = _os.lower().split()

                    _osName = _filteredOS[0]
                    _osVersion = _filteredOS[1]

                    if _osName in TargetDataManager.supportedOSVersion and any(_osVersion.startswith(x) for x in TargetDataManager.supportedOSVersion[_osName]):
                        target = TargetModel(IPAddress=_ip, hostName=_host, SSHUsername=_user, SSHPort=_port, SSHKey=_key, osVersionName=_os)
                    else:
                        continue

                    if self.model_manager.addNewTarget(target):
                        newTargetAdded += 1
                
                except Exception as e:
                    addWarningMsgBox(
                        self.main_window,
                        "Row Error",
                        f"Skipping row {i+2}: {str(e)}" # type: ignore
                    )
        
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
                f"Failed to read Excel file:\n{str(e)}"
            )

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

    def clearInput(self):
        self.view.IPAddressInput.clear()
        self.view.hostNameInput.clear()
        self.view.SSHKeyInput.clear()