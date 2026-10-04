import sys
from PyQt5 import QtWidgets
import config.config
from gui.mainwindow import MainWindow
b1 = config.config.getConfig()
def fonk1(args):
    b2 = QtWidgets.QApplication(sys.argv)
    b3 = MainWindow(b1)
    b3.show()
    b2.exec_()
if b4 = = "__main__":
    fonk1(sys.argv[1:])