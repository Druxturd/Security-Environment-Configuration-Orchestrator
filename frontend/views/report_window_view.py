from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QTabWidget,
    QDialogButtonBox,
    QWidget,
    QLabel,
    QTextEdit
)
from PySide6.QtCore import QSize
from ansi2html import Ansi2HTMLConverter
from views.detail_report_view import DetailReportView
from models.detail_report_tree_model import DetailReportModel
from controllers.detail_report_controller import DetailReportController

class ReportWindow(QDialog):
    def __init__(self, report_text: str, target_list: list):
        super().__init__()
        self.setWindowTitle("Ansible Playbook Report")
        self.setFixedSize(QSize(1280, 720))
        self.setModal(True)

        layout = QVBoxLayout()

        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.TabPosition.North)

        layout.addWidget(self.tabs)
        
        self.initSummaryTab(report_text)
        self.initDetailTab(target_list)

        QBtn = QDialogButtonBox.StandardButton.Close
        self.close_button = QDialogButtonBox(QBtn)
        self.close_button.rejected.connect(self.reject)
        layout.addWidget(self.close_button)

        self.setLayout(layout)

    def initSummaryTab(self, report_text: str):
        self.tab1 = QWidget()
        self.l1 = QVBoxLayout()
        self.title = QLabel("Playbook Result Report")
        self.l1.addWidget(self.title)

        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)
        self.text_area.setHtml(Ansi2HTMLConverter().convert(report_text))
        self.text_area.setAcceptRichText(True)
        self.l1.addWidget(self.text_area)
        self.tab1.setLayout(self.l1)
        self.tabs.addTab(self.tab1, "Summary")
    
    def initDetailTab(self, target_list: list):
        self.detailTab = DetailReportView()
        self.detailModel = DetailReportModel(target_list)
        self.detailController = DetailReportController(self.detailTab, self.detailModel)
        self.detailTab.show()

        self.tabs.addTab(self.detailTab, "Detail")