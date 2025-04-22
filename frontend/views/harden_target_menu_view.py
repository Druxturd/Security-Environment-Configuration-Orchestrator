from tabnanny import check
from PyQt5.QtWidgets import (
    QHBoxLayout, 
    QVBoxLayout, 
    QPushButton, 
    QLabel,
    QLineEdit,
    QWidget,
    QScrollArea,
    QCheckBox
)
from utils.layout_utils import *

class HardenTargetMenuView(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    # Function to init harden target menu UI
    def initUI(self):
        self.mainLayout = QVBoxLayout()

        self.hLayout1 = QHBoxLayout()
        self.hardenMenuLbl = QLabel("Harden Target Menu")
        self.autoHardenBtn = QPushButton("Execute Auto Harden")
        addWidgetToLayout(self.hardenMenuLbl, self.hLayout1)
        addWidgetToLayout(self.autoHardenBtn, self.hLayout1)

        self.vLayout1 = QVBoxLayout()
        self.hardenListLbl = QLabel("Harden List")

        # Scroll area
        self.scrollArea = QScrollArea()
        self.scrollArea.setFixedHeight(200)

        # Widget to store checklist of harden list
        self.contentWidget = QWidget()
        self.checkBoxLayout = QVBoxLayout(self.contentWidget)
        self.checkboxes = []
        self.contentWidget.setLayout(self.checkBoxLayout)
        self.scrollArea.setWidget(self.contentWidget)
        addWidgetToLayout(self.hardenListLbl, self.vLayout1)
        addWidgetToLayout(self.scrollArea, self.vLayout1)

        ############### temporary widget
        self.checkBtn = QPushButton("check")
        addWidgetToLayout(self.checkBtn, self.vLayout1)
        #########################

        self.hLayout2 = QHBoxLayout()
        self.executeHardenBtn = QPushButton("Execute Harden")
        self.totalTargetLbl = QLabel("Total Target: ")
        addWidgetToLayout(self.executeHardenBtn, self.hLayout2)
        addWidgetToLayout(self.totalTargetLbl, self.hLayout2)

        self.hLayout3 = QHBoxLayout()
        self.backBtn = QPushButton("Back to Main Menu")
        addWidgetToLayout(self.backBtn, self.hLayout3)
        addChildLayoutToParentLayout(self.hLayout2, self.hLayout3)
        
        addChildLayoutToParentLayout(self.hLayout1, self.mainLayout)
        addChildLayoutToParentLayout(self.vLayout1, self.mainLayout)
        addChildLayoutToParentLayout(self.hLayout3, self.mainLayout)

        self.setLayout(self.mainLayout)