from PyQt5.QtWidgets import (
    QMainWindow,
    QFileDialog
)

def uploadCSVHandler(main_window:QMainWindow):
    options = QFileDialog.Options()
    filePath, _ = QFileDialog.getOpenFileName(
        main_window,
        "Open CSV File",
        "",
        "CSV Files (*.csv)",
        options=options
    )

    if not filePath:
        
        return
    
