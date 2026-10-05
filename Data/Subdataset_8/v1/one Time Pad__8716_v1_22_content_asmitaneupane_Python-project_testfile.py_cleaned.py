import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QDialog, QMessageBox
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 status bar example - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar().showMessage('Message in statusbar.')
        button = QPushButton('Open Dialog', self)
        button.setToolTip('This is an example button')
        button.move(100, 70)
        button.clicked.connect(self.openDialog)
        self.show()
    def openDialog(self):
        dialog = Dialog()
        dialog.exec_()
class Dialog(QDialog):
    def __init__(self):
        super(Dialog, self).__init__()
        self.setWindowTitle('Dialog Example')
        self.setGeometry(100, 100, 200, 100)
        button = QPushButton('Click me', self)
        button.move(50, 30)
        button.clicked.connect(self.slot_method)
    def slot_method(self):
        QMessageBox.information(self, 'Message', 'Slot method is called.')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())