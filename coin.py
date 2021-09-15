from PySide2.QtWidgets import (
    QTextEdit,
    QWidget,
    QPushButton,
    QTextEdit
)
from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon
from utils import load_ui_widget

class Coin(QWidget):
    def __init__(self, filepath):

        super(Coin, self).__init__()
        load_ui_widget(filepath, self)
        self.setWindowTitle("Coin")
        self.setMinimumSize(QSize(615, 327))
        self.setMaximumSize(QSize(615, 327))
        self.btn = self.findChild(QPushButton, "pushButton_8")
        self.btn.clicked.connect(self.teste)

    # def cloesEvent(self, event):
    #    pass

    def teste(self):
        print("teste")
