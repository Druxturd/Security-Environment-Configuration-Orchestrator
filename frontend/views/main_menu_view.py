from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QHBoxLayout,
    QPushButton
)

class MainMenuView(QWidget):
    def __init__(self):
        super().__init__()

        self.main_layout = QVBoxLayout()
        self.main_menu_lbl = QLabel("Main Menu")

        self.target_list_layout = QHBoxLayout()
        self.target_list_menu_btn = QPushButton("Target List Menu")
        self.total_target_lbl = QLabel("Total Target: ")
        self.target_list_layout.addWidget(self.target_list_menu_btn)
        self.target_list_layout.addWidget(self.total_target_lbl)

        self.menu_layout = QHBoxLayout()
        self.harden_target_menu_btn = QPushButton("Harden Target Menu")
        self.patch_target_menu_btn = QPushButton("Patch Target Menu")
        self.menu_layout.addWidget(self.harden_target_menu_btn)
        self.menu_layout.addWidget(self.patch_target_menu_btn)

        self.main_layout.addWidget(self.main_menu_lbl)
        self.main_layout.addLayout(self.target_list_layout)
        self.main_layout.addLayout(self.menu_layout)

        self.setLayout(self.main_layout)