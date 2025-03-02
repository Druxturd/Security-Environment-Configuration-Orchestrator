from PyQt5.QtWidgets import (
    QHBoxLayout, 
    QVBoxLayout, 
    QPushButton, 
    QLabel,
    QWidget
)

class TargetListMenuView(QWidget):
    def __init__(self):
        super().__init__()

        self.mainLayout = QVBoxLayout()

        self.label = QLabel("Target List Menu")
        self.backBtn = QPushButton("Back to Main Menu")

        self.mainLayout.addWidget(self.label)
        self.mainLayout.addWidget(self.backBtn)

        self.setLayout(self.mainLayout)