import datetime
from models.target_model import TargetModel
from views.target_list_menu_view import TargetListMenuView
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime
import os
import requests

load_dotenv()
TEMPLATE_URL = f"{os.getenv("BACKEND_URL")}/download-template"

class TargetListMenuController:
    def __init__(self, view:TargetListMenuView, model:TargetModel, main_window):
        # Store the view, model, main window that being passed into the controller
        self.view = view
        self.model = model
        self.main_window = main_window

        self.errorMsg = [
            "IP Address must be fill!",
            "Host name must be fill!",
            "SSH Key must be fill"
        ]

        # Set the initial total target counter
        self.view.totalTargetLbl.setText(f"Total Target: {self.model.getCountTargetList()}")

        # Connect every button in harden target menu with respective function (e.g. backBtn when clicked will trigger function goToMainMenu)
        self.view.clearTargetBtn.clicked.connect(self.model.clearTargetList)
        self.view.downloadTemplateBtn.clicked.connect(self.downloadTemplate)
        self.view.addTargetBtn.clicked.connect(self.addTarget)
        self.view.backBtn.clicked.connect(self.goToMainMenu)

        # Receive signal to update total target counter when changes occur to the target list data
        self.model.targetListUpdated.connect(self.updateTotalTargetCounter)

    # Function to go back to main menu from target list menu
    def goToMainMenu(self):
        self.main_window.switchToMainMenu()

    # Function to update total target counter
    def updateTotalTargetCounter(self):
        self.view.totalTargetLbl.setText("Total Target: " + str(self.model.getCountTargetList()))

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
        
        except requests.exceptions.Timeout:
            print("timeout")
        except requests.exceptions.ConnectionError:
            print("connection error")
        except requests.exceptions.HTTPError as http_err:
            print(http_err)
        except Exception as e:
            print(e)

    # Function to add new target
    def addTarget(self):
        if self.validateInput():
            return
        else:
            newTarget = TargetModel(
                IPAddress=self.view.IPAddressInput.text(),
                hostName=self.view.hostNameInput.text(),
                SSHKey=self.view.SSHKeyInput.toPlainText()
            )
            self.model.addNewTarget(newTarget)
            # self.model.addCounter()
            self.updateTotalTargetCounter()
            self.clearInput()

    # Function to clear input
    def clearInput(self):
        self.view.IPAddressInput.clear()
        self.view.hostNameInput.clear()
        self.view.SSHKeyInput.clear()

    # Function to validate input
    def validateInput(self):
        if self.view.IPAddressInput.text().strip() == "":
            self.main_window.showError(self.errorMsg[0])
            return True
        elif self.view.hostNameInput.text().strip() == "":
            self.main_window.showError(self.errorMsg[1])
            return True
        elif self.view.SSHKeyInput.toPlainText().strip() == "":
            self.main_window.showError(self.errorMsg[2])
            return True
        else:
            return False