from PyQt5.QtWidgets import (
    QHBoxLayout, 
    QVBoxLayout, 
    QPushButton, 
    QLabel,
    QLineEdit,
    QTextEdit,
    QWidget
)
from utils.layout_util import *

class TargetListMenuView(QWidget):
    def __init__(self):
        super().__init__()
        
        self._initUI()

    # Function to ini target list menu UI
    def _initUI(self):

        self.mainLayout = QVBoxLayout()

        self.hLayout1 = QHBoxLayout()
        self.targetListMenuLbl = QLabel("Target List Menu")
        self.downloadTemplateBtn = QPushButton("Download Excel Template")
        self.uploadBtn = QPushButton("Upload Excel")
        addWidgetToLayout(self.targetListMenuLbl, self.hLayout1)
        addWidgetToLayout(self.downloadTemplateBtn, self.hLayout1)
        addWidgetToLayout(self.uploadBtn, self.hLayout1)
        ### temporary button
        self.checkBtn = QPushButton("Check")
        addWidgetToLayout(self.checkBtn, self.hLayout1)
        ########
        
        self.vLayout1 = QVBoxLayout()
        self.IPAddressLbl = QLabel("IP Address")
        self.IPAddressInput = QLineEdit()
        addWidgetToLayout(self.IPAddressLbl, self.vLayout1)
        addWidgetToLayout(self.IPAddressInput, self.vLayout1)

        self.vLayout2 = QVBoxLayout()
        self.hostNameLbl = QLabel("Host Name")
        self.hostNameInput = QLineEdit()
        addWidgetToLayout(self.hostNameLbl, self.vLayout2)
        addWidgetToLayout(self.hostNameInput, self.vLayout2)

        self.hLayout2 = QHBoxLayout()
        addChildLayoutToParentLayout(self.vLayout1, self.hLayout2)
        addChildLayoutToParentLayout(self.vLayout2, self.hLayout2)

        self.hLayout3 = QHBoxLayout()
        self.SSHKeyLbl = QLabel("SSH Key")
        self.SSHKeyInput = QTextEdit()
        addWidgetToLayout(self.SSHKeyLbl, self.hLayout3)
        addWidgetToLayout(self.SSHKeyInput, self.hLayout3)

        self.hLayout4 = QHBoxLayout()
        self.clearTargetBtn = QPushButton("Clear Target")
        self.addTargetBtn = QPushButton("Add Target")
        self.totalTargetLbl = QLabel("Total Target: ")
        addWidgetToLayout(self.clearTargetBtn, self.hLayout4)
        addWidgetToLayout(self.addTargetBtn, self.hLayout4)
        addWidgetToLayout(self.totalTargetLbl, self.hLayout4)

        self.hLayout5 = QHBoxLayout()
        self.backBtn = QPushButton("Back to Main Menu")
        addWidgetToLayout(self.backBtn, self.hLayout5)
        addChildLayoutToParentLayout(self.hLayout4, self.hLayout5)

        addChildLayoutToParentLayout(self.hLayout1, self.mainLayout)
        addChildLayoutToParentLayout(self.hLayout2, self.mainLayout)
        addChildLayoutToParentLayout(self.hLayout3, self.mainLayout)
        addChildLayoutToParentLayout(self.hLayout5, self.mainLayout)

        self.setLayout(self.mainLayout)