from PyQt5.QtWidgets import (
    QHBoxLayout, 
    QVBoxLayout, 
    QPushButton, 
    QLabel,
    QLineEdit,
    QWidget
)
from utils.layout_utils import *

class PatchTargetMenuView(QWidget):
    def __init__(self):
        super().__init__()

        self.mainLayout = QVBoxLayout()

        self.patchMenuLbl = QLabel("Patch Target Menu")

        self.vLayout1 = QVBoxLayout()
        self.patchListLbl = QLabel("Patch List")
        self.patchListInp = QLineEdit() # temporary placeholder
        addWidgetToLayout(self.patchListLbl, self.vLayout1)
        addWidgetToLayout(self.patchListInp, self.vLayout1)

        self.hLayout1 = QHBoxLayout()
        self.executePatchBtn = QPushButton("Execute Patch")
        self.totalTargetLbl = QLabel("Total Target: ")
        addWidgetToLayout(self.executePatchBtn, self.hLayout1)
        addWidgetToLayout(self.totalTargetLbl, self.hLayout1)

        self.hLayout2 = QHBoxLayout()
        self.backBtn = QPushButton("Back to Main Menu")
        addWidgetToLayout(self.backBtn, self.hLayout2)
        addChildLayoutToMainLayout(self.hLayout1, self.hLayout2)

        addWidgetToLayout(self.patchMenuLbl, self.mainLayout)
        addChildLayoutToMainLayout(self.vLayout1, self.mainLayout)
        addChildLayoutToMainLayout(self.hLayout2, self.mainLayout)

        self.setLayout(self.mainLayout)