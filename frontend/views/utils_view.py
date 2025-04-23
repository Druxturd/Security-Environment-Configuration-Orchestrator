from PyQt5.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QTextEdit
)
from PyQt5.QtCore import QSize
from utils.layout_utils import addWidgetToLayout
from ansi2html import Ansi2HTMLConverter

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

class ReportWindow(QDialog):
    def __init__(self, report_text: str):
        super().__init__()
        self.setWindowTitle("Ansible Playbook Report")
        self.setFixedSize(QSize(600, 400))
        self.setModal(True)

        layout = QVBoxLayout()

        self.title = QLabel("Playbook Result Report")
        addWidgetToLayout(self.title,layout)

        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)
        self.text_area.setHtml(Ansi2HTMLConverter().convert(report_text))
        self.text_area.setAcceptRichText(True)
        addWidgetToLayout(self.text_area, layout)

        self.close_button = QPushButton("Close")
        self.close_button.clicked.connect(self.accept)
        addWidgetToLayout(self.close_button, layout)

        self.setLayout(layout)