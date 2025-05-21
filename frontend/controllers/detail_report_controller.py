import json

from ansi2html import Ansi2HTMLConverter
from models.detail_report_tree_model import DetailReportModel
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
            if self.current_playbook["harden_control"]:
                _text += f"\nControl: {self.current_playbook['harden_control']}"
            self.view.text_area.setHtml(Ansi2HTMLConverter().convert(_text))
            self.view.text_area.moveCursor(QTextCursor.MoveOperation.End)

    def update_event_detail(self, key: str):
        if (
            self.current_playbook["events"]  # type: ignore
            and len(self.current_playbook["events"][key]) != 0  # type: ignore
        ):
            _text = "\n".join(
                f"TASK [{x['event_data']['task']}]\n"
                + (
                    self.format_looped_results(
                        x["event_data"]["host"], x["event_data"]["res"], x["event_data"]
                    )
                    if isinstance(x["event_data"].get("res", {}).get("results"), list)
                    else (
                        f"\x1b[0;36mskipping: [{x['event_data']['host']}]\x1b[0m"
                        if x["event_data"].get("event") == "runner_on_skipped"
                        else x.get("stdout", "")
                    )
                )
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

    def format_looped_results(self, ip: str, res: dict, event_data: dict):
        output_lines = []
        results = res.get("results", [])
        for result in results:
            if result.get("skipped", False):
                status = "skipping"
                color = "\x1b[0;36m"  # cyan
            elif result.get("failed", False):
                status = "failed"
                color = "\x1b[0;31m"  # red
            elif result.get("changed", False):
                status = "changed"
                color = "\x1b[0;33m"  # yellow
            else:
                status = "ok"
                color = "\x1b[0;32m"  # green

            item_lbl = result.get("_ansible_item_label", result.get("item"))
            item_part = f"(item={item_lbl})" if item_lbl else ""
            result_str = json.dumps(result, sort_keys=True, ensure_ascii=False)

            line = f"{color}{status}: [{ip}] => {item_part} => {result_str}\x1b[0m"
            output_lines.append(line)

            if result.get("failed") and event_data.get("ignore_errors", False):
                output_lines.append("\x1b[0;36m...ignoring\x1b[0m")

        return "\n".join(output_lines)
