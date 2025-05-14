from PySide6.QtCore import QObject, Qt
from PySide6.QtWidgets import QCheckBox
from views.select_target_view import SelectTargetView
from models.target_data_manager import TargetDataManager

class SelectTargetController(QObject):
    def __init__(self, view: SelectTargetView, model_manager: TargetDataManager, main_window):
        super().__init__()

        self.view = view
        self.model_manager = model_manager
        self.main_window = main_window

        self.view.select_all_btn.clicked.connect(self.select_all_target)
        self.view.select_all_btn.clicked.connect(self.view.reject)

        self.view.reset_btn.clicked.connect(self.reset_selection)

        self.view.confirm_btn.clicked.connect(self.confirm_selection)
        self.view.confirm_btn.clicked.connect(self.view.reject)

        self.view.close_btn.rejected.connect(self.view.reject)

        self.fetch_target_list()
        self.check_selection()

    def fetch_target_list(self):
        for target in self.model_manager.get_target_list():
            self.check_box = QCheckBox(target.to_selected_target_format())
            self.view.check_boxes.append(self.check_box)
            self.view.scroll_content_layout.addWidget(self.check_box)
        
        self.view.scroll_content.setFixedHeight(len(self.view.check_boxes) * 25)

        self.view.scroll_content.adjustSize()
        self.view.scroll_area.update()
        self.view.repaint()

    def select_all_target(self):
        self.model_manager.set_all_check_status_true()
        self.main_window.update_selected_target_counter()

    def check_selection(self):
        checked_list = []
        for target in self.model_manager.get_target_list():
            if target.is_checked:
                checked_list.append(target.to_selected_target_format())
        for cb in self.view.check_boxes:
            if cb.text() in checked_list:
                cb.setCheckState(Qt.CheckState.Checked)
    
    def reset_selection(self):
        for cb in self.view.check_boxes:
            if cb.isChecked():
                cb.setCheckState(Qt.CheckState.Unchecked)
        self.model_manager.reset_check_status()
        self.main_window.update_selected_target_counter()

    def confirm_selection(self):
        checked_list = []
        for cb in self.view.check_boxes:
            if cb.isChecked():
                checked_list.append(cb.text())
        for target in self.model_manager.get_target_list():
            if target.to_selected_target_format() in checked_list:
                target.is_checked = True
            else:
                target.is_checked = False
        
        self.main_window.update_selected_target_counter()