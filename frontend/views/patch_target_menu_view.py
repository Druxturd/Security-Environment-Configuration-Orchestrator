from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QHBoxLayout,
    QPushButton
)

class PatchTargetMenuView(QWidget):
    def __init__(self):
        super().__init__()

        self.main_layout = QVBoxLayout()

        self.patch_menu_lbl = QLabel("Patch Target Menu")
        self.main_layout.addWidget(self.patch_menu_lbl)

        self.vLayout1 = QVBoxLayout()
        self.patch_list_lbl = QLabel("Patch List")
        self.patch_list_input = QLineEdit() # temporary placeholder
        self.vLayout1.addWidget(self.patch_list_lbl)
        self.vLayout1.addWidget(self.patch_list_input)

        self.hLayout1 = QHBoxLayout()
        self.back_btn = QPushButton("Back to Main Menu")
        self.execute_patch_btn = QPushButton("Execute Patch")
        self.total_target_lbl = QLabel("Total Target(s): ")
        self.hLayout1.addWidget(self.back_btn)
        self.hLayout1.addWidget(self.execute_patch_btn)
        self.hLayout1.addWidget(self.total_target_lbl)

        self.main_layout.addLayout(self.vLayout1)
        self.main_layout.addLayout(self.hLayout1)

        self.setLayout(self.main_layout)