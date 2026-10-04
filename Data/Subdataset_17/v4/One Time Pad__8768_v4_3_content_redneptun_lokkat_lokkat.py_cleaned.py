import sys
from PyQt5 import QtWidgets
from config.config import getConfig
from gui.mainwindow import MainWindow
def main():
    active_config = getConfig()
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(active_config)
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()