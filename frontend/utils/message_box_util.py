from views.main_window_view import MainWindow

from PySide6.QtWidgets import QMessageBox, QMainWindow

def center_msg_box(box: QMessageBox, parent: MainWindow | QMainWindow):
    parent_geometry = parent.frameGeometry()
    box_geometry = box.frameGeometry()
    box_geometry.moveCenter(parent_geometry.center())
    box.move(box_geometry.topLeft())
    box.exec()

def add_information_msg_box(main_window: MainWindow | QMainWindow, title: str, msg: str):
    box = QMessageBox(main_window)
    box.setIcon(QMessageBox.Icon.Information)
    box.setWindowTitle(title)
    box.setText(msg)
    center_msg_box(box, main_window)

def add_critical_msg_box(main_window: MainWindow | QMainWindow, title: str, msg: str):
    box = QMessageBox(main_window)
    box.setIcon(QMessageBox.Icon.Critical)
    box.setWindowTitle(title)
    box.setText(msg)
    center_msg_box(box, main_window)

def add_warning_msg_box(main_window: MainWindow | QMainWindow, title: str, msg: str):
    box = QMessageBox(main_window)
    box.setIcon(QMessageBox.Icon.Warning)
    box.setWindowTitle(title)
    box.setText(msg)
    center_msg_box(box, main_window)