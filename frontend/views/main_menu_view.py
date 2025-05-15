from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton
)
from PySide6.QtCore import Qt

class MainMenuView(QWidget):
    def __init__(self):
        super().__init__()

        self.main_layout = QVBoxLayout()

        self.main_menu_lbl = QLabel("Main Menu")
        self.total_target_lbl = QLabel("Total Target: ")
        for label in (self.main_menu_lbl, self.total_target_lbl):
            label.setFixedHeight(label.sizeHint().height())
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.main_layout.addWidget(label)

        self.target_list_menu_btn = QPushButton("Target List Menu")
        self.harden_target_menu_btn = QPushButton("Harden Target Menu")
        self.patch_target_menu_btn = QPushButton("Patch Target Menu")
        for button in (self.target_list_menu_btn, self.harden_target_menu_btn, self.patch_target_menu_btn):
            button.setFixedHeight(button.sizeHint().height())
            self.main_layout.addWidget(button)

        self.setLayout(self.main_layout)