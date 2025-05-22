from models.target_data_manager import TargetDataManager
from views.show_target_list_view import ShowTargetList

from PySide6.QtCore import QObject, Qt
from PySide6.QtWidgets import QCheckBox, QMessageBox


class ShowTargetListController(QObject):
    def __init__(self, view: ShowTargetList, model_manager: TargetDataManager):
        super().__init__()
        self.view = view
        self.model_manager = model_manager

        self.view.remove_btn.clicked.connect(self.remove_selected_target)

        self.view.clear_btn.clicked.connect(self.clear_target_list)

        self.view.close_btn.rejected.connect(self.view.reject)

        self.fetch_target_list()
        self.update_total_target_counter()

    def fetch_target_list(self):
        for target in self.model_manager.get_target_list():
            self.check_box = QCheckBox(target.to_selected_target_format())
            self.view.check_boxes.append(self.check_box)
            self.view.scroll_content_layout.addWidget(self.check_box)

        self.view.scroll_content.setFixedHeight(len(self.view.check_boxes) * 25)

        self.view.scroll_content.adjustSize()
        self.view.scroll_area.update()
        self.view.repaint()

    def update_total_target_counter(self):
        self.view.total_target_lbl.setText(
            f"Total Target(s): {self.model_manager.get_count_target_list()}"
        )

    def reset_selection(self):
        for cb in self.view.check_boxes:
            if cb.isChecked():
                cb.setCheckState(Qt.CheckState.Unchecked)

    def remove_selected_target(self):
        checked_list = []
        for cb in self.view.check_boxes:
            if cb.isChecked():
                checked_list.append(cb.text())
        for target in self.model_manager.get_target_list():
            if target.to_selected_target_format() in checked_list:
                self.model_manager.remove_selected_target(target)
        if checked_list:
            self.update_total_target_counter()
            QMessageBox.information(
                self.view,
                "Remove Selected Target Successful",
                f"Selected target(s) have been removed from the list\nTotal target(s): {self.model_manager.get_count_target_list()}",
            )
            self.view.reject()
        else:
            QMessageBox.information(
                self.view,
                "Remove Selected Target Failed",
                "Please select a target to remove",
            )

    def clear_target_list(self):
        self.model_manager.clear_target_list()
        self.update_total_target_counter()
        QMessageBox.information(
            self.view, "Clear Target Successful", "Target list has been cleared"
        )
        self.view.reject()
