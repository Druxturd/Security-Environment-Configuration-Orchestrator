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

        self.patch_menu_lbl = QLabel("Patch Target Menu")
        self.main_layout.addWidget(self.patch_menu_lbl)

        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.TabPosition.North)
        self.main_layout.addWidget(self.tabs)

        self.init_patch_all_host_tab()
        self.init_patch_specific_host_tab()

        ### TO BE DELETE
        self.hLayout1 = QHBoxLayout()
        self.back_btn = QPushButton("Back to Main Menu")
        self.execute_patch_btn = QPushButton("Execute Patch")
        self.hLayout1.addWidget(self.back_btn)
        self.hLayout1.addWidget(self.execute_patch_btn)

        self.main_layout.addLayout(self.hLayout1)
        ##############

        self.setLayout(self.main_layout)
    
    def init_patch_all_host_tab(self):
        self.all_tab = QWidget()
        self.all_tab_layout = QVBoxLayout()

        self.total_target_lbl = QLabel("Total Target(s): ")

        self.all_combo_box_layout = QHBoxLayout()
        self.all_combo_box_lbl = QLabel("All Host Playbook:")
        self.all_combo_box_lbl.setFixedWidth(self.all_combo_box_lbl.sizeHint().width())
        self.all_playbook_combo_box = QComboBox()
        self.all_combo_box_layout.addWidget(self.all_combo_box_lbl)
        self.all_combo_box_layout.addWidget(self.all_playbook_combo_box)

        self.all_detail_widget = QWidget()
        self.all_detail_widget_layout = QVBoxLayout()
        self.all_detail_widget.setLayout(self.all_detail_widget_layout)
        
        self.all_tab_layout.addWidget(self.total_target_lbl)
        self.all_tab_layout.addLayout(self.all_combo_box_layout)
        self.all_tab_layout.addWidget(self.all_detail_widget)

        self.all_tab.setLayout(self.all_tab_layout)
        
        self.tabs.addTab(self.all_tab, "All Host")

    def init_patch_specific_host_tab(self):
        self.specific_tab = QWidget()
        self.specific_tab_layout = QVBoxLayout()
        self.selected_target_layout = QHBoxLayout()
        self.total_selected_target_lbl = QLabel(f"Total Selected Target(s): 0")
        self.select_target_btn = QPushButton("Select Target")
        self.selected_target_layout.addWidget(self.total_selected_target_lbl)
        self.selected_target_layout.addWidget(self.select_target_btn)

        self.specific_combo_box_layout = QHBoxLayout()
        self.specific_combo_box_lbl = QLabel("Specific Host Playbook:")
        self.specific_combo_box_lbl.setFixedWidth(self.specific_combo_box_lbl.sizeHint().width())
        self.specific_playbook_combo_box = QComboBox()
        self.specific_combo_box_layout.addWidget(self.specific_combo_box_lbl)
        self.specific_combo_box_layout.addWidget(self.specific_playbook_combo_box)

        self.specific_detail_widget = QWidget()
        self.specific_detail_widget_layout = QVBoxLayout()
        self.specific_detail_widget.setLayout(self.specific_detail_widget_layout)

        self.specific_tab_layout.addLayout(self.selected_target_layout)
        self.specific_tab_layout.addLayout(self.specific_combo_box_layout)
        self.specific_tab_layout.addWidget(self.specific_detail_widget)

        self.specific_tab.setLayout(self.specific_tab_layout)

        self.tabs.addTab(self.specific_tab, "Specific Host")