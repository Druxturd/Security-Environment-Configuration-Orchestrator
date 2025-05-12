from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea
)

class HardenTargetMenuView(QWidget):
    def __init__(self):
        super().__init__()

        self.main_layout = QVBoxLayout()

        self.upper_layout = QHBoxLayout()
        self.harden_menu_lbl = QLabel("Harden Target Menu")
        self.auto_harden_btn = QPushButton("Execute Auto Harden")

        self.upper_layout.addWidget(self.harden_menu_lbl)
        self.upper_layout.addWidget(self.auto_harden_btn)

        self.harden_list_layout = QVBoxLayout()
        self.harden_list_lbl = QLabel("Harden List")
        self.scroll_area = QScrollArea()
        self.scroll_area.setFixedHeight(200)

        self.scroll_content = QWidget()
        self.scroll_content_layout = QVBoxLayout(self.scroll_content)
        # self.scroll_content_layout.setParent(self.scroll_content)

        self.check_boxes = []
        self.scroll_content.setLayout(self.scroll_content_layout)
        self.scroll_area.setWidget(self.scroll_content)

        self.harden_list_layout.addWidget(self.harden_list_lbl)
        self.harden_list_layout.addWidget(self.scroll_area)

        self.bottom_layout = QHBoxLayout()
        self.back_btn = QPushButton("Back to Main Menu")
        self.execute_harden_btn = QPushButton("Execute Harden")
        self.total_target_list_lbl = QLabel("Total Target(s): ")
        self.bottom_layout.addWidget(self.back_btn)
        self.bottom_layout.addWidget(self.execute_harden_btn)
        self.bottom_layout.addWidget(self.total_target_list_lbl)

        self.main_layout.addLayout(self.upper_layout)
        self.main_layout.addLayout(self.harden_list_layout)
        self.main_layout.addLayout(self.bottom_layout)

        self.setLayout(self.main_layout)