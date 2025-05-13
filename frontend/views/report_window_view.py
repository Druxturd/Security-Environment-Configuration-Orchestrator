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
from models.report_model import ReportModel
from models.detail_report_tree_model import DetailReportModel
from controllers.detail_report_controller import DetailReportController

class ReportWindowView(QDialog):
    def __init__(self, report_text: str, target_list: list[ReportModel]):
        super().__init__()
        self.setWindowTitle("Ansible Playbook Report")
        self.setFixedSize(QSize(1280, 720))
        self.setModal(True)

        layout = QVBoxLayout()

        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.TabPosition.North)

        layout.addWidget(self.tabs)
        
        self.init_summary_tab(report_text)
        self.init_detail_tab(target_list)

        QBtn = QDialogButtonBox.StandardButton.Close
        self.close_button = QDialogButtonBox(QBtn)
        self.close_button.rejected.connect(self.reject)
        layout.addWidget(self.close_button)

        self.setLayout(layout)

    def init_summary_tab(self, report_text: str):
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
    
    def init_detail_tab(self, target_list: list):
        self.detail_tab = DetailReportView()
        self.detail_model = DetailReportModel(target_list)
        self.detail_controller = DetailReportController(self.detail_tab, self.detail_model)
        self.detail_tab.show()

        self.tabs.addTab(self.detail_tab, "Detail")