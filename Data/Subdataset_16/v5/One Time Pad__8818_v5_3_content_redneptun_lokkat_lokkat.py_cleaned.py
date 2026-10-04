import sys
from PyQt5 import QtWidgets
from config.config import getConfig
from gui.mainwindow import MainWindow
def fonk1():
    b1 = getConfig()
    b2 = QtWidgets.QApplication(sys.argv)
    b3 = MainWindow(b1)
    return b2, b3
def fonk2():
    b2, b3 = fonk1()
    b3.show()
    sys.exit(b2.exec_())
if b4 = = "__main__":
    fonk2()