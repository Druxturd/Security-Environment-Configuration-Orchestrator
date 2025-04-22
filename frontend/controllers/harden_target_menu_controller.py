from PyQt5.QtCore import QObject, Qt
from PyQt5.QtWidgets import QCheckBox,QProgressDialog, QMessageBox
import httpx
from qasync import asyncSlot
from models.target_data_manager import TargetDataManager
from views.harden_target_menu_view import HardenTargetMenuView
from views.report_window import ReportWindow
from utils.layout_utils import *
from dotenv import load_dotenv
import os
import requests

load_dotenv()
HARDEN_LIST_URL = f"{os.getenv("BACKEND_URL")}/harden"
EXECUTE_SELECTED_HARDEN_URL = f"{HARDEN_LIST_URL}/execute"

class HardenTargetMenuController(QObject):
    def __init__(self, view:HardenTargetMenuView, model_manager:TargetDataManager, main_window):
        # Store the view, model manager, main window that being passed into the controller
        super().__init__()
        self.view = view
        self.model_manager = model_manager
        self.main_window = main_window
        
        # Set the initial total target counter
        self.view.totalTargetLbl.setText(f"Total Target: {self.model_manager.getCountTargetList()}")

        # Connect every button in harden target menu with respective function (e.g. backBtn when clicked will trigger function goToMainMenu)
        self.view.backBtn.clicked.connect(self.goToMainMenu)

        ### temporary button to check selectd item(s)
        self.view.checkBtn.clicked.connect(self.checkItem)
        
        # execute selected playbook
        self.view.executeHardenBtn.clicked.connect(self.executeSelectedHarden) # type: ignore

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
    
    # Function to execute harden list
    @asyncSlot()
    async def executeSelectedHarden(self):
        self.view.executeHardenBtn.setEnabled(False)
        progress = QProgressDialog("Running playbooks...", None, 0, 0,self.main_window, Qt.WindowType.FramelessWindowHint)
        progress.setWindowTitle("Please wait")
        progress.setModal(True)
        progress.setCancelButton(None)
        progress.setEnabled(False)
        progress.show()
        payload = {
            "playbooks": [cb.text() for cb in self.view.checkboxes if cb.isChecked()],
            "targets": self.model_manager.getPayload()
        }
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(EXECUTE_SELECTED_HARDEN_URL, json=payload)
                result = response.json()
        except httpx.TimeoutException:
            result = {"error": "Requrest timed out."}
        except Exception as e:
            result = {"error:", e}
        finally:
            progress.close()
        
        if "error" in result:
            QMessageBox.critical(self.main_window, "Erorr", result["error"]) # type: ignore
        else:
            report = "\n\n".join(
                f"IPAddress: {x['host']}\nPlaybook: {y['playbook']}\nStatus: {y['Status']}\nrc: {y['rc']}\nOutput: {y['stdout']}" for x in result['results'] for y in x['results'] # type: ignore
            )
            dialog = ReportWindow(report)
            dialog.exec()
        self.uncheckAllSelectedItems()
        self.view.executeHardenBtn.setEnabled(True)


    ### temporary function to check selected item(s)
    def checkItem(self):
        checked = [cb.text() for cb in self.view.checkboxes if cb.isChecked()]
        print("Checked: ", checked)
    ##############

    def uncheckAllSelectedItems(self):
        for cb in self.view.checkboxes:
            if cb.isChecked():
                cb.setCheckState(Qt.CheckState.Unchecked)
