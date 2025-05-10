from PyQt5.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QDialogButtonBox,
    QTextEdit,
    QTabWidget,
    QWidget,
)
from PyQt5.QtCore import QSize
from utils.layout_util import *
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

        addWidgetToLayout(self.tabs, layout)
        
        self.initSummaryTab(report_text)
        self.initDetailTab(target_list)

        QBtn = QDialogButtonBox.StandardButton.Close
        self.close_button = QDialogButtonBox(QBtn)
        self.close_button.rejected.connect(self.reject)
        addWidgetToLayout(self.close_button, layout)

        self.setLayout(layout)

    def initSummaryTab(self, report_text: str):
        self.tab1 = QWidget()
        self.l1 = QVBoxLayout()
        self.title = QLabel("Playbook Result Report")
        addWidgetToLayout(self.title, self.l1)

        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)
        self.text_area.setHtml(Ansi2HTMLConverter().convert(report_text))
        self.text_area.setAcceptRichText(True)
        addWidgetToLayout(self.text_area, self.l1)
        self.tab1.setLayout(self.l1)
        self.tabs.addTab(self.tab1, "Summary")
    
    def initDetailTab(self, target_list: list):
        self.detailTab = DetailReportView()
        self.detailModel = DetailReportModel(target_list)
        self.detailController = DetailReportController(self.detailTab, self.detailModel)
        self.detailTab.show()

        self.tabs.addTab(self.detailTab, "Detail")