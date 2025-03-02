from PyQt5.QtWidgets import (
    QHBoxLayout, 
    QVBoxLayout, 
    QPushButton, 
    QLabel,
    QWidget
)

class MainMenuView(QWidget):
    def __init__(self):
        super().__init__()

        self.mainLayout = QVBoxLayout()

        self.hLayout1 = QHBoxLayout()
        self.hLayout2 = QHBoxLayout()

        self.totalTargetLbl = QLabel("Total target: ")

        self.targetListMenuBtn = QPushButton("Target List Menu")
        self.hardenTargetMenuBtn = QPushButton("Harden Target Menu")
        self.patchTargetMenuBtn = QPushButton("Patch Target Menu")

        self.hLayout1.addWidget(self.targetListMenuBtn)
        self.hLayout1.addWidget(self.totalTargetLbl)

        self.hLayout2.addWidget(self.hardenTargetMenuBtn)
        self.hLayout2.addWidget(self.patchTargetMenuBtn)
        
        self.mainLayout.addLayout(self.hLayout1)
        self.mainLayout.addLayout(self.hLayout2)

        self.setLayout(self.mainLayout)