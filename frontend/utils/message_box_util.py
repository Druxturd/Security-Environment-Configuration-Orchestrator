from views.main_window_view import MainWindow

from PySide6.QtWidgets import QMessageBox, QMainWindow

def center_msg_box(box: QMessageBox, parent: MainWindow | QMainWindow):
    box.adjustSize()
    parent_center = parent.frameGeometry().center()
    box_geometry = box.frameGeometry()
    box_geometry.moveCenter(parent_center)
    box.move(box_geometry.topLeft())

def add_information_msg_box(main_window: MainWindow | QMainWindow, title: str, msg: str):
    box = QMessageBox(main_window)
    box.setIcon(QMessageBox.Icon.Information)
    box.setWindowTitle(title)
    box.setText(msg)
    center_msg_box(box, main_window)
    box.exec()

def add_critical_msg_box(main_window: MainWindow | QMainWindow, title: str, msg: str):
    box = QMessageBox(main_window)
    box.setIcon(QMessageBox.Icon.Critical)
    box.setWindowTitle(title)
    box.setText(msg)
    center_msg_box(box, main_window)
    box.exec()

def add_warning_msg_box(main_window: MainWindow | QMainWindow, title: str, msg: str):
    box = QMessageBox(main_window)
    box.setIcon(QMessageBox.Icon.Warning)
    box.setWindowTitle(title)
    box.setText(msg)
    center_msg_box(box, main_window)
    box.exec()