from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QTextEdit
)

class TargetListMenuView(QWidget):
    def __init__(self):
        super().__init__()

        self.main_layout = QVBoxLayout()

        self.upper_layout = QHBoxLayout()
        self.target_list_menu_lbl = QLabel("Target List Menu")
        self.download_template_btn = QPushButton("Download Excel Template")
        self.upload_excel_btn = QPushButton("Upload Excel")
        self.upper_layout.addWidget(self.target_list_menu_lbl)
        self.upper_layout.addWidget(self.download_template_btn)
        self.upper_layout.addWidget(self.upload_excel_btn)

        self.middle_layout = QVBoxLayout()

        self.ip_layout = QVBoxLayout()
        self.ip_lbl = QLabel("IP Address")
        self.ip_input = QLineEdit()
        self.ip_layout.addWidget(self.ip_lbl)
        self.ip_layout.addWidget(self.ip_input)

        self.host_layout = QVBoxLayout()
        self.host_lbl = QLabel("Host Name")
        self.host_input = QLineEdit()
        self.host_layout.addWidget(self.host_lbl)
        self.host_layout.addWidget(self.host_input)

        self.upper_mid_layout = QHBoxLayout()
        self.upper_mid_layout.addLayout(self.ip_layout)
        self.upper_mid_layout.addLayout(self.host_layout)

        self.key_layout = QHBoxLayout()
        self.key_lbl = QLabel("SSH Private Key")
        self.key_input = QTextEdit()
        self.key_layout.addWidget(self.key_lbl)
        self.key_layout.addWidget(self.key_input)

        self.middle_layout.addLayout(self.upper_mid_layout)
        self.middle_layout.addLayout(self.key_layout)

        self.bottom_layout = QHBoxLayout()
        self.back_btn = QPushButton("Back to Main Menu")
        self.clear_target_btn = QPushButton("Clear Target")
        self.add_target_btn = QPushButton("Add Target")
        self.total_target_lbl = QLabel("Total Target: ")
        self.bottom_layout.addWidget(self.back_btn)
        self.bottom_layout.addWidget(self.clear_target_btn)
        self.bottom_layout.addWidget(self.add_target_btn)
        self.bottom_layout.addWidget(self.total_target_lbl)

        self.main_layout.addLayout(self.upper_layout)
        self.main_layout.addLayout(self.middle_layout)
        self.main_layout.addLayout(self.bottom_layout)

        self.setLayout(self.main_layout)