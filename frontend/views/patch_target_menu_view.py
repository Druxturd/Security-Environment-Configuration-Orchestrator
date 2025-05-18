from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTabWidget,
    QComboBox,
    QHBoxLayout,
    QPushButton,
    QLineEdit,
    QSizePolicy
)

class PatchTargetMenuView(QWidget):
    def __init__(self):
        super().__init__()

        self.main_layout = QVBoxLayout()

        self.patch_content_layout = QVBoxLayout()
        self.patch_menu_lbl = QLabel("Patch Target Menu")
        self.patch_content_layout.addWidget(self.patch_menu_lbl)

        self.total_target_lbl = QLabel("Total Target(s): ")
        self.patch_content_layout.addWidget(self.total_target_lbl)

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
        
        ### TO BE DELETE
        self.hLayout1 = QHBoxLayout()
        self.back_btn = QPushButton("Back to Main Menu")
        self.execute_patch_btn = QPushButton("Execute Patch")
        self.hLayout1.addWidget(self.back_btn)
        self.hLayout1.addWidget(self.execute_patch_btn)

        self.main_layout.addLayout(self.hLayout1)
        ##############

        self.setLayout(self.main_layout)