import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from StartUi import Ui_MainWindow

if __name__ == "__main__":
    app = QApplication([])
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())