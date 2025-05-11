from views.detail_report_view import DetailReportView
from PyQt5.QtCore import QModelIndex
from PyQt5.QtGui import QTextCursor
from ansi2html import Ansi2HTMLConverter

class DetailReportController:
    def __init__(self, view: DetailReportView, model):
        self.view = view
        self.model = model
        self.view.columnView.setModel(self.model)
        self.view.columnView.updateGeometry()
        
        self.currentPlaybook = None

        self.view.columnView.selectionModel().currentChanged.connect(self.onCurrentChanged)
        self.view.okBtn.clicked.connect(lambda: self.updateEventDetail("ok"))
        self.view.failedBtn.clicked.connect(lambda: self.updateEventDetail("failed"))
        self.view.unreachableBtn.clicked.connect(lambda: self.updateEventDetail("unreachable"))
        self.view.skippedBtn.clicked.connect(lambda: self.updateEventDetail("skipped"))
        # self.view.statusBtn.clicked.connect(lambda: self.updateDetail("status"))
        # self.view.rcBtn.clicked.connect(lambda: self.updateDetail("rc"))
        self.view.summaryBtn.clicked.connect(lambda: self.updateDetail("stdout"))
        
    def onCurrentChanged(self, index: QModelIndex):
        item = index.internalPointer()
        data = item.data()
        if data["type"] == "playbook":
            self.currentPlaybook = data["details"]
            self.updateDetail("stdout")
            self.view.summaryBtn.setChecked(True)
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
            self.view.text_area.setHtml(Ansi2HTMLConverter().convert(f"{self.currentPlaybook[key]}"))
            self.view.text_area_cursor.movePosition(QTextCursor.MoveOperation.End)
    
    def updateEventDetail(self, key: str):
        if self.currentPlaybook['events'] and len(self.currentPlaybook['events'][key]) != 0:
            _text = "\n".join(
                f"TASK [{x['event_data']['task']}]\n{x['stdout']}" for x in self.currentPlaybook['events'][key]
            )
            self.view.text_area.setHtml(Ansi2HTMLConverter().convert(_text))
        else:
            self.view.text_area.setHtml(Ansi2HTMLConverter().convert(f"There is no information about {key} event(s)"))
        self.view.text_area_cursor.movePosition(QTextCursor.MoveOperation.End)