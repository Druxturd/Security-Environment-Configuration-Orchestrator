from views.detail_report_view import DetailReportView
from PyQt5.QtCore import QModelIndex, QTimer
from ansi2html import Ansi2HTMLConverter

class DetailReportController:
    def __init__(self, view: DetailReportView, model):
        self.view = view
        self.model = model
        self.view.columnView.setModel(self.model)
        self.view.columnView.updateGeometry()
        
        self.currentPlaybook = None

        self.view.columnView.selectionModel().currentChanged.connect(self.onCurrentChanged)
        self.view.statusBtn.clicked.connect(lambda: self.updateDetail("status"))
        self.view.rcBtn.clicked.connect(lambda: self.updateDetail("rc"))
        self.view.stdoutBtn.clicked.connect(lambda: self.updateDetail("stdout"))
        
    def onCurrentChanged(self, index: QModelIndex):
        item = index.internalPointer()
        data = item.data()
        if data["type"] == "playbook":
            self.currentPlaybook = data["details"]
            self.updateDetail("stdout")
            self.view.stdoutBtn.setChecked(True)
            for btn in self.view.btnGroup.buttons():
                btn.setEnabled(True)
        else:
            self.currentPlaybook = None
            self.view.text_area.setHtml(Ansi2HTMLConverter().convert("Select a playbook to see details"))
            for btn in self.view.btnGroup.buttons():
                btn.setEnabled(False)
                btn.setChecked(False)
    
    def updateDetail(self, key: str):
        if self.currentPlaybook:
            self.view.text_area.setHtml(Ansi2HTMLConverter().convert(f"{key.capitalize()}: {self.currentPlaybook[key]}"))