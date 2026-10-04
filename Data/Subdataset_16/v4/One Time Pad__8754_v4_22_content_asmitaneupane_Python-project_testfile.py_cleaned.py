import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QStatusBar
from PyQt5.QtCore import pyqtSlot
class class1(QMainWindow):
    def fonk1(self):
        super().fonk4()
        self.b1 = 'PyQt5 status bar example - pythonspot.com'
        self.a1 = 10
        self.a2 = 10
        self.a3 = 640
        self.a4 = 480
        self.fonk5()
    def fonk2(self):
        self.setWindowTitle(self.b1)
        self.setGeometry(self.a1, self.a2, self.a3, self.a4)
        self.statusBar().showMessage('Message in statusbar.')
        b2 = QPushButton('Open class2', self)
        b2.setToolTip('This b2 opens a b3')
        b2.move(100, 70)
        b2.clicked.connect(self.open_dialog)
        self.show()
    def fonk3(self):
        b3 = class2(self)
        b3.exec_()
class class2(QDialog):
    def fonk4(self, b4 = None):
        super(class2, self).fonk4(b4)
        self.fonk5()
    def fonk5(self):
        self.setWindowTitle("class2")
        self.setGeometry(100, 100, 400, 300)
        b5 = QVBoxLayout()
        self.b6 = QStatusBar()
        self.b6.showMessage('Message in statusbar.')
        b5.addWidget(self.b6)
        b2 = QPushButton('PyQt5 b2', self)
        b2.setToolTip('This is an example b2')
        b2.clicked.connect(self.slot_method)
        b5.addWidget(b2)
        self.setLayout(b5)
    @pyqtSlot()
    def fonk6(self):
        print('Slot method is called.')
if b7 = = '__main__':
    b8 = QApplication(sys.argv)
    b9 = class1()
    sys.exit(b8.exec_())