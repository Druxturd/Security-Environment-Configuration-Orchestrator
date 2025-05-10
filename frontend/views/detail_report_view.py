from PyQt5.QtWidgets import QWidget, QHBoxLayout, QColumnView, QAbstractItemView, QLabel, QTextEdit, QButtonGroup, QPushButton, QAbstractScrollArea, QSizePolicy
from PyQt5.QtCore import Qt

from utils.layout_util import *

from ansi2html import Ansi2HTMLConverter

class DetailReportView(QWidget):
    def __init__(self):
        super().__init__()
        self.mainLayout = QHBoxLayout()
        self.setLayout(self.mainLayout)

        self.columnView = QColumnView()
        self.columnView.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.columnView.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.columnView.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        self.columnView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.columnView.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerItem)
        self.columnView.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        self.columnView.setTabKeyNavigation(False)
        self.columnView.setColumnWidths([215, 215, 0])
        addWidgetToLayout(self.columnView, self.mainLayout)

        self.detailWidget = QWidget()
        self.detailLayout = QVBoxLayout()
        self.detailWidget.setLayout(self.detailLayout)
        self.detailWidget.setFixedWidth(640)
        addWidgetToLayout(self.detailWidget, self.mainLayout)

        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)
        self.text_area.setHtml(Ansi2HTMLConverter().convert("Select a playbook to see details"))
        self.text_area.setAcceptRichText(True)
        addWidgetToLayout(self.text_area, self.detailLayout)

        self.btnLayout = QHBoxLayout()
        addChildLayoutToParentLayout(self.btnLayout, self.detailLayout)

        self.btnGroup = QButtonGroup()
        self.btnGroup.setExclusive(True)

        self.statusBtn = QPushButton("Show Status")
        self.rcBtn = QPushButton("Show RC")
        self.stdoutBtn = QPushButton("Show Stdout")

        for btn in (self.statusBtn, self.rcBtn, self.stdoutBtn):
            addWidgetToLayout(btn, self.btnLayout)
            self.btnGroup.addButton(btn)
            btn.setCheckable(True)
            btn.setEnabled(False)
            btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)