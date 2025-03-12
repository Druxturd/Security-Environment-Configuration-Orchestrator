from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QPushButton
)
from utils.layout_utils import *

class ErrorView(QDialog):
    def __init__(self, message):
        super().__init__()
        self.setWindowTitle("Error!")
        self.setFixedSize(QSize(300, 150))
        self.setModal(True)

        layout = QVBoxLayout()
        self.errorLbl = QLabel(message)
        self.closeBtn = QPushButton("Close")
        self.closeBtn.clicked.connect(self.accept)

        addWidgetToLayout(self.errorLbl, layout)
        addWidgetToLayout(self.closeBtn, layout)

        self.setLayout(layout)