from PyQt5.QtWidgets import (
    QMainWindow, 
    QApplication, 
    QHBoxLayout, 
    QVBoxLayout, 
    QPushButton, 
    QLabel,
    QWidget
)

def HardenMenu(self):
        self.setWindowTitle("SECOR - Harden Menu")

        vLayout1 = QVBoxLayout()

        totalTargetLbl = QLabel()
        totalTargetLbl.setText("Total Target: " + str(self.totalTarget))

        hardenTargetBtn = QPushButton()
        hardenTargetBtn.setText("back Target")
        hardenTargetBtn.clicked.connect(self.goToMainMenu)

        vLayout1.addWidget(totalTargetLbl)
        vLayout1.addWidget(hardenTargetBtn)

        widget = QWidget()
        widget.setLayout(vLayout1)
        self.setCentralWidget(widget)