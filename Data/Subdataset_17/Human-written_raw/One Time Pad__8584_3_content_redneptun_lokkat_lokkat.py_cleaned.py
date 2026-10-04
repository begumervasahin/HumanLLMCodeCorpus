import sys
from PyQt5 import QtWidgets
import config.config
from gui.mainwindow import MainWindow
activeConfig = config.config.getConfig()
def main(args):
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(activeConfig)
    window.show()
    app.exec_()
if __name__ == "__main__":
    main(sys.argv[1:])