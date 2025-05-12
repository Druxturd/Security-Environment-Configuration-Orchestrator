from views.detail_report_view import DetailReportView
from PySide6.QtCore import QModelIndex
from PySide6.QtGui import QTextCursor
from ansi2html import Ansi2HTMLConverter

class DetailReportController:
    def __init__(self, view: DetailReportView, model):
        self.view = view
        self.model = model
        self.view.column_view.setModel(self.model)
        self.view.column_view.updateGeometry()
        
        self.currentPlaybook = None

        self.view.column_view.selectionModel().currentChanged.connect(self.onCurrentChanged)
        self.view.ok_btn.clicked.connect(lambda: self.updateEventDetail("ok"))
        self.view.failed_btn.clicked.connect(lambda: self.updateEventDetail("failed"))
        self.view.unreachable_btn.clicked.connect(lambda: self.updateEventDetail("unreachable"))
        self.view.skipped_btn.clicked.connect(lambda: self.updateEventDetail("skipped"))
        # self.view.status_btn.clicked.connect(lambda: self.updateDetail("status"))
        # self.view.rc_btn.clicked.connect(lambda: self.updateDetail("rc"))
        self.view.summary_btn.clicked.connect(lambda: self.updateDetail("stdout"))
    
    def onCurrentChanged(self, index: QModelIndex):
        item = index.internalPointer()
        data = item.data()
        if data["type"] == "playbook":
            self.current_playbook = data["details"]
            self.updateDetail("stdout")
            self.view.summary_btn.setChecked(True)
            for btn in self.view.btn_group.buttons():
                btn.setEnabled(True)
        else:
            self.current_playbook = None
            self.view.text_area.setHtml(Ansi2HTMLConverter().convert("Select a playbook to see details"))
            for btn in self.view.btn_group.buttons():
                btn.setEnabled(False)
                btn.setChecked(False)
    
    def updateDetail(self, key: str):
        if self.current_playbook:
            self.view.text_area.setHtml(Ansi2HTMLConverter().convert(f"{self.current_playbook[key]}"))
            self.view.text_area.moveCursor(QTextCursor.MoveOperation.End)
    
    def updateEventDetail(self, key: str):
        if self.current_playbook['events'] and len(self.current_playbook['events'][key]) != 0: # type: ignore
            _text = "\n".join(
                f"TASK [{x['event_data']['task']}]\n{x['stdout']}" for x in self.current_playbook['events'][key] # type: ignore
            )
            self.view.text_area.setHtml(Ansi2HTMLConverter().convert(_text))
        else:
            self.view.text_area.setHtml(Ansi2HTMLConverter().convert(f"There is no information about {key} event(s)"))
        self.view.text_area.moveCursor(QTextCursor.MoveOperation.End)