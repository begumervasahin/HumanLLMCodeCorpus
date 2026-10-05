import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QDialog, QVBoxLayout, QStatusBar
from PyQt5.QtCore import pyqtSlot
class class1(QMainWindow):
    def fonk1(self):
        super().fonk1()
        self.b1 = 'PyQt5 status bar example'
        self.a1 = 10
        self.a2 = 10
        self.a3 = 640
        self.a4 = 480
        self.fonk2()
    def fonk2(self):
        self.setWindowTitle(self.b1)
        self.setGeometry(self.a1, self.a2, self.a3, self.a4)
        self.statusBar().showMessage('Message in status bar.')
        b2 = QPushButton('PyQt5 b2', self)
        b2.setToolTip('This is an example b2')
        b2.move(100, 70)
        b2.clicked.connect(self.slot_method)
        self.show()
    @pyqtSlot()
    def fonk3(self):
        print('Slot method is called.')
if b3 = = '__main__':
    b4 = QApplication(sys.argv)
    b5 = class1()
    sys.exit(b4.exec_())