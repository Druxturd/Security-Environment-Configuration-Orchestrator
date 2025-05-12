from views.main_window_view import MainWindow

from PySide6.QtWidgets import QMessageBox, QMainWindow

def add_information_msg_box(main_window: MainWindow | QMainWindow, title: str, msg: str):
    QMessageBox.information(main_window, title, msg)

def add_critical_msg_box(main_window: MainWindow | QMainWindow, title: str, msg: str):
    QMessageBox.critical(main_window, title, msg)

def add_warning_msg_box(main_window: MainWindow | QMainWindow, title: str, msg: str):
    QMessageBox.warning(main_window, title, msg)