from PySide6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class PatchTargetMenuView(QWidget):
    def __init__(self):
        super().__init__()

        self.main_layout = QVBoxLayout()

        self.patch_content_layout = QVBoxLayout()
        self.header_patch_layout = QHBoxLayout()
        self.patch_menu_lbl = QLabel("Patch Target Menu")
        self.total_target_lbl = QLabel("Total Target(s): ")
        self.header_patch_layout.addWidget(self.patch_menu_lbl)
        self.header_patch_layout.addWidget(self.total_target_lbl)

        self.patch_content_layout.addLayout(self.header_patch_layout)

        self.combo_box_layout = QHBoxLayout()
        self.combo_box_lbl = QLabel("Select Playbook:")
        self.combo_box_lbl.setFixedWidth(self.combo_box_lbl.sizeHint().width())
        self.playbook_combo_box = QComboBox()
        self.combo_box_layout.addWidget(self.combo_box_lbl)
        self.combo_box_layout.addWidget(self.playbook_combo_box)
        self.patch_content_layout.addLayout(self.combo_box_layout)

        self.detail_widget = QWidget()
        self.detail_widget_layout = QVBoxLayout()
        self.detail_widget.setLayout(self.detail_widget_layout)
        self.patch_content_layout.addWidget(self.detail_widget)

        self.main_layout.addLayout(self.patch_content_layout)

        self.hLayout1 = QHBoxLayout()
        self.back_btn = QPushButton("Back to Main Menu")
        self.execute_patch_btn = QPushButton("Execute Patch")
        self.hLayout1.addWidget(self.back_btn)
        self.hLayout1.addWidget(self.execute_patch_btn)

        self.main_layout.addLayout(self.hLayout1)

        self.setLayout(self.main_layout)
