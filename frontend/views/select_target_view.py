from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QWidget,
    QDialogButtonBox
)
from PySide6.QtCore import Qt

class SelectTargetView(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Select Target")

        layout = QVBoxLayout()

        self.upper_layout = QHBoxLayout()
        self.select_target_menu_lbl = QLabel("Select Target")
        self.select_all_btn = QPushButton("Select All")
        self.upper_layout.addWidget(self.select_target_menu_lbl)
        self.upper_layout.addWidget(self.select_all_btn)

        self.target_list_layout = QVBoxLayout()
        self.target_list_lbl = QLabel("Target List")
        self.scroll_area = QScrollArea()
        self.scroll_area.setFixedHeight(200)

        self.scroll_content = QWidget()
        self.scroll_content_layout = QVBoxLayout(self.scroll_content)

        self.check_boxes = []
        self.scroll_content.setLayout(self.scroll_content_layout)
        self.scroll_area.setWidget(self.scroll_content)

        self.target_list_layout.addWidget(self.target_list_lbl)
        self.target_list_layout.addWidget(self.scroll_area)

        self.lower_layout = QHBoxLayout()
        self.close_btn = QDialogButtonBox(QDialogButtonBox.StandardButton.Close)
        
        self.reset_btn = QPushButton("Reset Selection")
        self.confirm_btn = QPushButton("Confirm Target")

        self.lower_layout.addWidget(self.close_btn)
        self.lower_layout.addWidget(self.reset_btn)
        self.lower_layout.addWidget(self.confirm_btn)

        layout.addLayout(self.upper_layout)
        layout.addLayout(self.target_list_layout)
        layout.addLayout(self.lower_layout)

        self.setLayout(layout)
    
    def keyPressEvent(self, event):
        key = event.key()

        if key in (Qt.Key.Key_Escape, Qt.Key.Key_Return, Qt.Key.Key_Enter):
            event.ignore()
        else:
            super().keyPressEvent(event)