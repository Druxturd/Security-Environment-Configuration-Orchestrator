from PySide6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

SUPPORTED_OS = ["Debian 12", "Ubuntu 22", "Ubuntu 24"]


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

        self.os_version_name_layout = QVBoxLayout()
        self.os_version_lbl = QLabel("OS Version Name")
        self.os_version_name_combo_box = QComboBox()
        for i, data in enumerate(SUPPORTED_OS):
            self.os_version_name_combo_box.insertItem(i, data, data)
        self.os_version_name_layout.addWidget(self.os_version_lbl)
        self.os_version_name_layout.addWidget(self.os_version_name_combo_box)

        self.upper_mid_layout = QHBoxLayout()
        self.upper_mid_layout.addLayout(self.ip_layout)
        self.upper_mid_layout.addLayout(self.host_layout)
        self.upper_mid_layout.addLayout(self.os_version_name_layout)

        self.ssh_username_layout = QVBoxLayout()
        self.ssh_username_lbl = QLabel("SSH Username")
        self.ssh_username_input = QLineEdit()
        self.ssh_username_layout.addWidget(self.ssh_username_lbl)
        self.ssh_username_layout.addWidget(self.ssh_username_input)

        self.password_layout = QVBoxLayout()
        self.password_lbl = QLabel("Password")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_layout.addWidget(self.password_lbl)
        self.password_layout.addWidget(self.password_input)

        self.port_layout = QVBoxLayout()
        self.port_lbl = QLabel("Port (Default port is 22 if empty)")
        self.port_input = QLineEdit()
        self.port_layout.addWidget(self.port_lbl)
        self.port_layout.addWidget(self.port_input)

        self.upper_mid_layout_2 = QHBoxLayout()
        self.upper_mid_layout_2.addLayout(self.ssh_username_layout)
        self.upper_mid_layout_2.addLayout(self.password_layout)
        self.upper_mid_layout_2.addLayout(self.port_layout)

        self.key_layout = QHBoxLayout()
        self.key_lbl = QLabel("SSH Private Key")
        self.key_input = QTextEdit()
        self.key_input.setAcceptRichText(False)
        self.key_layout.addWidget(self.key_lbl)
        self.key_layout.addWidget(self.key_input)

        self.middle_layout.addLayout(self.upper_mid_layout)
        self.middle_layout.addLayout(self.upper_mid_layout_2)
        self.middle_layout.addLayout(self.key_layout)

        self.bottom_layout = QHBoxLayout()
        self.back_btn = QPushButton("Back to Main Menu")
        self.view_target_list_btn = QPushButton("View Target List")
        self.add_target_btn = QPushButton("Add Target")
        self.total_target_lbl = QLabel("Total Target: ")
        self.bottom_layout.addWidget(self.back_btn)
        self.bottom_layout.addWidget(self.view_target_list_btn)
        self.bottom_layout.addWidget(self.add_target_btn)
        self.bottom_layout.addWidget(self.total_target_lbl)

        self.main_layout.addLayout(self.upper_layout)
        self.main_layout.addLayout(self.middle_layout)
        self.main_layout.addLayout(self.bottom_layout)

        self.setLayout(self.main_layout)
