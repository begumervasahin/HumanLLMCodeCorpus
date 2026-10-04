import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QStatusBar, QDialog, QVBoxLayout
from PyQt5.QtCore import pyqtSlot
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 Status Bar Example - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar().showMessage('Message in status bar.')
        button = QPushButton('Open Dialog', self)
        button.setToolTip('This opens a dialog')
        button.move(100, 70)
        button.clicked.connect(self.openDialog)
        self.show()
    def openDialog(self):
        self.dialog = Dialog()
        self.dialog.exec_()
class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.title = 'Dialog'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 240
        self.initUI()
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('Message in status bar.')
        button = QPushButton('PyQt5 Button', self)
        button.setToolTip('This is an example button')
        button.move(100, 70)
        button.clicked.connect(self.slot_method)
    @pyqtSlot()
    def slot_method(self):
        print('Slot method is called.')
    def setStatusBar(self, statusbar):
        self.statusbar = statusbar
        layout = self.layout() or QVBoxLayout()
        layout.addWidget(statusbar)
        self.setLayout(layout)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())