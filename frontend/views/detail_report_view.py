from PySide6.QtWidgets import(
    QWidget,
    QHBoxLayout,
    QColumnView,
    QAbstractItemView,
    QAbstractScrollArea,
    QSizePolicy,
    QVBoxLayout,
    QTextEdit,
    QButtonGroup,
    QPushButton
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QTextCursor
from ansi2html import Ansi2HTMLConverter

class DetailReportView(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)

        self.column_view = QColumnView()
        self.column_view.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.column_view.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.column_view.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        self.column_view.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.column_view.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerItem)
        self.column_view.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        self.column_view.setTabKeyNavigation(False)
        self.column_view.setColumnWidths([200, 200, 0])
        self.main_layout.addWidget(self.column_view)

        self.detail_widget = QWidget()
        self.detail_layout = QVBoxLayout()
        self.detail_widget.setLayout(self.detail_layout)
        self.detail_widget.setFixedWidth(680)
        self.main_layout.addWidget(self.detail_widget)

        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)
        self.text_area.setHtml(Ansi2HTMLConverter().convert("Select a playbook to see details"))
        self.text_area.setAcceptRichText(True)
        self.detail_layout.addWidget(self.text_area)

        self.btn_layout = QVBoxLayout()
        self.detail_layout.addLayout(self.btn_layout)

        self.btn_group = QButtonGroup()
        self.btn_group.setExclusive(True)

        self.summary_btn = QPushButton("Summary")
        self.ok_btn = QPushButton("Ok Event(s)")
        self.failed_btn = QPushButton("Failed Event(s)")
        self.unreachable_btn = QPushButton("Unreachable Event(s)")
        self.skipped_btn = QPushButton("Skipped Event(s)")

        for btn in (self.summary_btn, self.ok_btn, self.failed_btn, self.unreachable_btn, self.skipped_btn):
            self.btn_layout.addWidget(btn)
            self.btn_group.addButton(btn)
            btn.setCheckable(True)
            btn.setEnabled(False)
            btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)