from PySide2.QtWidgets import (
    QApplication,
    QMainWindow,
    QMdiArea,
    QMdiSubWindow,
    QTextEdit,
    QAction,
    QDesktopWidget,
    QWidget,
    QDialog,
    QPushButton,
)
from PySide2 import QtCore
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, QSize
import sys
from PySide2.QtGui import QIcon


def load_ui_widget(filename, parent):
    loader = QUiLoader()
    uifile = QFile(filename)
    uifile.open(QFile.ReadOnly)
    loader.load(uifile, parent)
    uifile.close()


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


class Cliente(QWidget):
    def __init__(self, filepath):
        super(Cliente, self).__init__()
        load_ui_widget(filepath, self)
        self.setWindowTitle("Cliente")
        self.setMinimumSize(QSize(615, 327))
        self.setMaximumSize(QSize(615, 327))


# our main window class
class WindowWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.formCoin = None
        self.formCliente = None

        # title, geoemtry and icon for this window
        self.setWindowTitle("Pyside2 MDI Window")
        self.setGeometry(100, 100, 900, 500)
        self.setWindowIcon(QIcon("pyicon.png"))

        # creating object of MDI
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        # our menu bar
        menu_bar = self.menuBar()

        # our menu items
        file = menu_bar.addMenu("File")
        file.addAction("Coin")
        file.addAction("Cliente")
        file.addAction("Cascade")
        # file.addAction("Tiled")
        file.triggered[QAction].connect(self.window_triggered)
        self.showMaximized()

    def loadSubWindow(self, widget):
        window = self.mdi.addSubWindow(widget)
        window.setFixedSize(window.size())
        window.setWindowFlags(
            QtCore.Qt.Dialog
            | QtCore.Qt.WindowCloseButtonHint
            | QtCore.Qt.WindowMinimizeButtonHint
            | QtCore.Qt.CustomizeWindowHint
        )
        window.move(
            (self.mdi.width() - window.width() - 10) / 2,
            (self.mdi.height() - window.height() - 90) / 2,
        )
        window.show()

    def findMdiChild(self, fileName):
        for window in self.mdi.subWindowList():
            if window.widget().windowTitle() == fileName:
                return window
        return None

    def window_triggered(self, p):
         if p.text() == "Coin":
            existing = self.findMdiChild('Coin')
            if existing is None:
                self.formCoin = Coin("coin.ui")
                self.loadSubWindow(self.formCoin)
            else:
                self.formCoin.setFocus()
 
         if p.text() == "Cliente":
            existing = self.findMdiChild('Cliente')
            if existing is None:
                self.formCliente = Cliente("clienteform.ui")
                self.loadSubWindow(self.formCliente)
            else:
                self.formCliente.setFocus()

         if p.text() == "Cascade":            
             self.mdi.cascadeSubWindows()
         if p.text() == "Tiled":
             self.mdi.tileSubWindows()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WindowWidget()
    sys.exit(app.exec_())
