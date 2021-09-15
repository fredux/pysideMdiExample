from PySide2.QtWidgets import (
    QTextEdit,
    QWidget,
    QPushButton,
)
from PySide2.QtCore import QSize
from utils import load_ui_widget

class Cliente(QWidget):
    def __init__(self, filepath):
        super(Cliente, self).__init__()
        load_ui_widget(filepath, self)
        self.setWindowTitle("Cliente")
        self.setMinimumSize(QSize(615, 327))
        self.setMaximumSize(QSize(615, 327))

