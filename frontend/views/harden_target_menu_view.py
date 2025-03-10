from PyQt5.QtWidgets import (
    QHBoxLayout, 
    QVBoxLayout, 
    QPushButton, 
    QLabel,
    QLineEdit,
    QWidget
)
from utils.layout_utils import *

class HardenTargetMenuView(QWidget):
    def __init__(self):
        super().__init__()

        self.mainLayout = QVBoxLayout()

        self.hLayout1 = QHBoxLayout()
        self.hardenMenuLbl = QLabel("Harden Target Menu")
        self.autoHardenBtn = QPushButton("Execute Auto Harden")
        addWidgetToLayout(self.hardenMenuLbl, self.hLayout1)
        addWidgetToLayout(self.autoHardenBtn, self.hLayout1)

        self.vLayout1 = QVBoxLayout()
        self.hardenListLbl = QLabel("Harden List")
        self.hardenListInp = QLineEdit() # temporary placeholder
        addWidgetToLayout(self.hardenListLbl, self.vLayout1)
        addWidgetToLayout(self.hardenListInp, self.vLayout1)

        self.hLayout2 = QHBoxLayout()
        self.executeHardenBtn = QPushButton("Execute Harden")
        self.totalTargetLbl = QLabel("Total Target: ")
        addWidgetToLayout(self.executeHardenBtn, self.hLayout2)
        addWidgetToLayout(self.totalTargetLbl, self.hLayout2)

        self.hLayout3 = QHBoxLayout()
        self.backBtn = QPushButton("Back to Main Menu")
        addWidgetToLayout(self.backBtn, self.hLayout3)
        addChildLayoutToMainLayout(self.hLayout2, self.hLayout3)
        
        addChildLayoutToMainLayout(self.hLayout1, self.mainLayout)
        addChildLayoutToMainLayout(self.vLayout1, self.mainLayout)
        addChildLayoutToMainLayout(self.hLayout3, self.mainLayout)

        self.setLayout(self.mainLayout)