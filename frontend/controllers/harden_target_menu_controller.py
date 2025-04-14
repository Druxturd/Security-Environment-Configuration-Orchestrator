from PyQt5.QtWidgets import QCheckBox
from models.target_data_manager import TargetDataManager
from views.harden_target_menu_view import HardenTargetMenuView
from utils.layout_utils import *
from dotenv import load_dotenv
import os
import requests

load_dotenv()
HARDEN_LIST_URL = f"{os.getenv("BACKEND_URL")}/harden"

class HardenTargetMenuController:
    def __init__(self, view:HardenTargetMenuView, model_manager:TargetDataManager, main_window):
        # Store the view, model manager, main window that being passed into the controller
        self.view = view
        self.model_manager = model_manager
        self.main_window = main_window
        
        # Set the initial total target counter
        self.view.totalTargetLbl.setText(f"Total Target: {self.model_manager.getCountTargetList()}")

        # Connect every button in harden target menu with respective function (e.g. backBtn when clicked will trigger function goToMainMenu)
        self.view.backBtn.clicked.connect(self.goToMainMenu)

        # Receive signal to update total target counter when changes occur to the target list data
        self.model_manager.targetListUpdated.connect(self.updateTotalTargetCounter)

        self.fetchFiles()

    # Function to go to the main menu from harden target menu
    def goToMainMenu(self):
        self.main_window.switchToMainMenu()

    # Function to update total target counter in main menu
    def updateTotalTargetCounter(self):
        self.view.totalTargetLbl.setText("Total Target: " + str(self.model_manager.getCountTargetList()))

    # Function to fetch harden list
    def fetchFiles(self):
        try:
            resp = requests.get(HARDEN_LIST_URL)
            if resp.status_code == 200:
                data = resp.json()
                dataList = data.get("harden_list", [])
                dataList.sort()
                for x in dataList:
                    self.checkBox = QCheckBox(x)
                    self.view.checkboxes.append(self.checkBox)
                    addWidgetToLayout(self.checkBox, self.view.checkBoxLayout)
                
                # Dynamically adjust the height of scrollable content
                self.view.contentWidget.setFixedHeight(len(self.view.checkboxes) * 25)

                # Refresh the UI
                self.view.contentWidget.adjustSize()
                self.view.scrollArea.update()
                self.view.repaint()

        except requests.exceptions.RequestException as e:
            print(e)
