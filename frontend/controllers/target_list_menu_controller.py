from models.target_model import TargetModel
from views.target_list_menu_view import TargetListMenuView

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
        self.view.addTargetBtn.clicked.connect(self.addTarget) # temporary add function
        self.view.backBtn.clicked.connect(self.goToMainMenu)

        # Receive signal to update total target counter when changes occur to the target list data
        self.model.targetListUpdated.connect(self.updateTotalTargetCounter)

    # Function to go back to main menu from target list menu
    def goToMainMenu(self):
        self.main_window.switchToMainMenu()

    # Function to update total target counter
    def updateTotalTargetCounter(self):
        self.view.totalTargetLbl.setText("Total Target: " + str(self.model.getCountTargetList()))

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