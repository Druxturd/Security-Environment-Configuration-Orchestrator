from PyQt5.QtWidgets import (
    QHBoxLayout, 
    QVBoxLayout,
    QWidget
)

def addWidgetToLayout(widget:QWidget, layout:QHBoxLayout | QVBoxLayout):
    layout.addWidget(widget)

def addChildLayoutToMainLayout(childLayout: QHBoxLayout | QVBoxLayout, mainLayout: QHBoxLayout | QVBoxLayout):
    mainLayout.addLayout(childLayout)