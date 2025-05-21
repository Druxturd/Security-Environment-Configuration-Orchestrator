import re
from collections import defaultdict

from ansi2html import Ansi2HTMLConverter
from models.detail_report_tree_model import DetailReportModel
from models.playbook_model import SelectedHardenPlaybookModel
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
        self.view.changed_btn.clicked.connect(
            lambda: self.update_event_detail("changed")
        )
        self.view.failed_btn.clicked.connect(lambda: self.update_event_detail("failed"))
        self.view.unreachable_btn.clicked.connect(
            lambda: self.update_event_detail("unreachable")
        )
        self.view.skipped_btn.clicked.connect(
            lambda: self.update_event_detail("skipping")
        )
        self.view.summary_btn.clicked.connect(lambda: self.update_detail("stdout"))

    def on_current_changed(self, index: QModelIndex):
        item = index.internalPointer()
        data = item.data()
        if data["type"] == "playbook":
            self.current_playbook = data["details"]
            self.raw_output = self.current_playbook["stdout"]
            self.status_grouped_output = self.extract_all_status_blocks(self.raw_output)
            self.group_html_by_status = self.convert_grouped_ansi_blocks_to_html(
                self.status_grouped_output
            )
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
            if isinstance(self.current_playbook, SelectedHardenPlaybookModel):
                _text += f"\nControl: {self.current_playbook['harden_control']}"
            self.view.text_area.setHtml(Ansi2HTMLConverter().convert(_text))
            self.view.text_area.moveCursor(QTextCursor.MoveOperation.End)

    def update_event_detail(self, key: str):
        if key in self.group_html_by_status.keys():
            self.view.text_area.setHtml(self.group_html_by_status[key])
        else:
            self.view.text_area.setHtml(
                Ansi2HTMLConverter().convert(
                    f"There is no information about {key} event(s)"
                )
            )
        self.view.text_area.moveCursor(QTextCursor.MoveOperation.End)

    def extract_all_status_blocks(self, ansible_stdout: str, statuses=None) -> dict:
        if statuses is None:
            statuses = [
                "ok",
                "changed",
                "skipping",
                "failed",
                "unreachable",
                "rescued",
                "ignored",
            ]

        # Exclude PLAY RECAP and anything after it
        ansible_stdout = re.split(
            r"^PLAY RECAP \*{5,}.*$", ansible_stdout, maxsplit=1, flags=re.MULTILINE
        )[0]

        # Match full task blocks including multiline output using DOTALL
        task_block_pattern = re.compile(
            r"(TASK \[.*?\] \*{3,}\n.*?)(?=TASK \[|\Z)", re.DOTALL
        )

        blocks = defaultdict(list)
        matches = task_block_pattern.findall(ansible_stdout)

        for block in matches:
            for status in statuses:
                # Use regex to match status at the beginning of a line for accuracy
                if re.search(rf"^\s*{re.escape(status)}:", block, re.DOTALL):
                    blocks[status].append(block)
                    break  # Only classify into one status group

        return blocks

    def convert_grouped_ansi_blocks_to_html(self, blocks: dict) -> dict:
        conv = Ansi2HTMLConverter()
        html_output = {}

        for status, block_list in blocks.items():
            combined = "\n".join(block_list)
            html_output[status] = conv.convert(combined)

        return html_output
