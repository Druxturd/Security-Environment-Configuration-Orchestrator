from PyQt5.QtWidgets import (
    QHBoxLayout, 
    QVBoxLayout,
    QWidget,
)

# Function to add widget to layout
def addWidgetToLayout(widget:QWidget, layout:QHBoxLayout | QVBoxLayout):
    layout.addWidget(widget)

# Function to add child layout to parent layout
def addChildLayoutToParentLayout(childLayout: QHBoxLayout | QVBoxLayout, mainLayout: QHBoxLayout | QVBoxLayout):
    mainLayout.addLayout(childLayout)