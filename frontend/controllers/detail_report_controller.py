from ansi2html import Ansi2HTMLConverter
from models.detail_report_tree_model import DetailReportModel
from models.playbook_model import SelectedHardenPlaybookModel, SemiHardenPlaybookModel
from views.detail_report_view import DetailReportView

from PySide6.QtCore import QModelIndex
from PySide6.QtGui import QTextCursor


class DetailReportController:
    def __init__(self, view: DetailReportView, model: DetailReportModel):
        self.view = view
        self.model = model
        self.view.column_view.setModel(self.model)
        self.view.column_view.updateGeometry()

        self.current_playbook = None

        self.view.column_view.selectionModel().currentChanged.connect(
            self.on_current_changed
        )
        self.view.ok_btn.clicked.connect(lambda: self.update_event_detail("ok"))
        self.view.failed_btn.clicked.connect(lambda: self.update_event_detail("failed"))
        self.view.unreachable_btn.clicked.connect(
            lambda: self.update_event_detail("unreachable")
        )
        self.view.skipped_btn.clicked.connect(
            lambda: self.update_event_detail("skipped")
        )
        self.view.summary_btn.clicked.connect(lambda: self.update_detail("stdout"))

    def on_current_changed(self, index: QModelIndex):
        item = index.internalPointer()
        data = item.data()
        if data["type"] == "playbook":
            self.current_playbook = data["details"]
            self.raw_output = self.current_playbook["stdout"]
            self.update_detail("stdout")
            self.view.summary_btn.setChecked(True)
            for btn in self.view.btn_group.buttons():
                btn.setEnabled(True)
        else:
            self.current_playbook = None
            self.view.text_area.setHtml(
                Ansi2HTMLConverter().convert("Select a playbook to see details")
            )
            for btn in self.view.btn_group.buttons():
                btn.setEnabled(False)
                btn.setChecked(False)

    def update_detail(self, key: str):
        if self.current_playbook:
            _text = f"{self.current_playbook[key]}\nStatus: {self.current_playbook['status']}"
            if isinstance(
                self.current_playbook, SelectedHardenPlaybookModel
            ) or isinstance(self.current_playbook, SemiHardenPlaybookModel):
                _text += f"\nControl: {self.current_playbook['harden_control']}"
            self.view.text_area.setHtml(Ansi2HTMLConverter().convert(_text))
            self.view.text_area.moveCursor(QTextCursor.MoveOperation.End)

    def update_event_detail(self, key: str):
        if self.current_playbook["events"] and self.current_playbook["events"][key]:  # type: ignore
            _text = "\n".join(
                f"TASK [{x['event_data']['task']}]\n{x['stdout']}"
                for x in self.current_playbook["events"][key]  # type: ignore
            )
            self.view.text_area.setHtml(Ansi2HTMLConverter().convert(_text))
        else:
            self.view.text_area.setHtml(
                Ansi2HTMLConverter().convert(
                    f"There is no information about {key} event(s)"
                )
            )
        self.view.text_area.moveCursor(QTextCursor.MoveOperation.End)
