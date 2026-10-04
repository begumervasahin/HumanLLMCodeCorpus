import sys
from PyQt5 import QtWidgets
import config.config
from gui.mainwindow import MainWindow
def main(args) -> None:
    active_config = config.config.getConfig()
    app = QtWidgets.QApplication(args)
    window = MainWindow(active_config)
    window.show()
    app.exec_()
if __name__ == "__main__":
    main(sys.argv)