import sys
from PySide2.QtUiTools import QUiLoader
from PySide2 import QtWidgets, QtCore


class MyApp(QtWidgets.QMainWindow):

    def initUI(self, ui_file):
        uifile = QtCore.QFile(ui_file)
        # uifile.open(QtCore.QFile.ReadOnly)

        loader = QUiLoader()
        self.window = loader.load(uifile)
        # uifile.close()

        self.window.pushButton_8.clicked.connect(self.CalculateTax)
        self.window.setWindowTitle("Halim")
        self.window.show()

    def CalculateTax(self):
        print('teste')

    def __init__(self, ui_file):
        super(MyApp, self).__init__()
        self.initUI(ui_file)


def main():
    app = QtWidgets.QApplication(sys.argv)
    myappl = MyApp("coin.ui")
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
