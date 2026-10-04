import sys
from PyQt5 import QtWidgets
import config.config
from gui.mainwindow import MainWindow
def fonk1(args) -> None:
    b1 = config.config.getConfig()
    b2 = QtWidgets.QApplication(args)
    b3 = MainWindow(b1)
    b3.show()
    b2.exec_()
if b4 = = "__main__":
    fonk1(sys.argv)