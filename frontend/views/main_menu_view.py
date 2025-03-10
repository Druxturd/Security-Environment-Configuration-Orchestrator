from PyQt5.QtWidgets import (
    QHBoxLayout, 
    QVBoxLayout, 
    QPushButton, 
    QLabel,
    QWidget
)
from utils.layout_utils import *

class MainMenuView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    # Function to init main menu UI
    def initUI(self):
        self.mainLayout = QVBoxLayout()

        self.mainMenuLbl = QLabel("Main Menu")

        self.hLayout1 = QHBoxLayout()
        self.targetListMenuBtn = QPushButton("Target List Menu")
        self.totalTargetLbl = QLabel("Total target: ")
        addWidgetToLayout(self.targetListMenuBtn, self.hLayout1)
        addWidgetToLayout(self.totalTargetLbl, self.hLayout1)

        self.hLayout2 = QHBoxLayout()
        self.hardenTargetMenuBtn = QPushButton("Harden Target Menu")
        self.patchTargetMenuBtn = QPushButton("Patch Target Menu")
        addWidgetToLayout(self.hardenTargetMenuBtn, self.hLayout2)
        addWidgetToLayout(self.patchTargetMenuBtn, self.hLayout2)

        addWidgetToLayout(self.mainMenuLbl, self.mainLayout)
        addChildLayoutToParentLayout(self.hLayout1, self.mainLayout)
        addChildLayoutToParentLayout(self.hLayout2, self.mainLayout)

        self.setLayout(self.mainLayout)