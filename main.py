from coin import Coin
from cliente import Cliente
import sys

from PySide2.QtWidgets import (
    QApplication,
    QMainWindow,
    QMdiArea,
    QMdiSubWindow,
    QAction,
    QDesktopWidget,
    QWidget,
    QDialog,
)
from PySide2.QtGui import QIcon
from PySide2 import QtCore


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
