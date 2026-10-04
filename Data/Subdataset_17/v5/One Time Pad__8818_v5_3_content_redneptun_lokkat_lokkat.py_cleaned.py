import sys
from PyQt5 import QtWidgets
from config.config import getConfig
from gui.mainwindow import MainWindow
def initialize_application():
    active_config = getConfig()
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(active_config)
    return app, window
def main():
    app, window = initialize_application()
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()