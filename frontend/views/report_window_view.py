from ansi2html import Ansi2HTMLConverter
from controllers.detail_report_controller import DetailReportController
from models.detail_report_tree_model import DetailReportModel
from models.report_model import ReportModel, SelectedHardenReportModel

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QLabel,
    QTabWidget,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)
from views.detail_report_view import DetailReportView


class ReportWindowView(QDialog):
    def __init__(self, report_text: str, target_list: list[ReportModel] | list[SelectedHardenReportModel]):
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

    def keyPressEvent(self, event):
        key = event.key()

        if key in (Qt.Key.Key_Escape, Qt.Key.Key_Return, Qt.Key.Key_Enter):
            event.ignore()
        else:
            super().keyPressEvent(event)

    def init_summary_tab(self, report_text: str):
        self.summary_tab = QWidget()
        self.summary_tab_layout = QVBoxLayout()
        self.title = QLabel("Playbook Result Report")
        self.summary_tab_layout.addWidget(self.title)

        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)
        self.text_area.setHtml(Ansi2HTMLConverter().convert(report_text))
        self.text_area.setAcceptRichText(True)
        self.summary_tab_layout.addWidget(self.text_area)
        self.summary_tab.setLayout(self.summary_tab_layout)
        self.tabs.addTab(self.summary_tab, "Summary")

    def init_detail_tab(self, target_list: list):
        self.detail_tab = DetailReportView()
        self.detail_model = DetailReportModel(target_list)
        self.detail_controller = DetailReportController(
            self.detail_tab, self.detail_model
        )
        self.detail_tab.show()

        self.tabs.addTab(self.detail_tab, "Detail")
