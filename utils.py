from PySide2 import QtCore
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile


def load_ui_widget(filename, parent):
    loader = QUiLoader()
    uifile = QFile(filename)
    uifile.open(QFile.ReadOnly)
    loader.load(uifile, parent)
    uifile.close()
