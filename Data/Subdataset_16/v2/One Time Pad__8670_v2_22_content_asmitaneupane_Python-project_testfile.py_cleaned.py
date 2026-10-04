import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QStatusBar, QDialog, QVBoxLayout
from PyQt5.QtCore import pyqtSlot
class class1(QMainWindow):
    def fonk1(self):
        super().fonk4()
        self.b1 = 'PyQt5 Status Bar Example - pythonspot.com'
        self.a1 = 10
        self.a2 = 10
        self.a3 = 640
        self.a4 = 480
        self.fonk5()
    def fonk2(self):
        self.setWindowTitle(self.b1)
        self.setGeometry(self.a1, self.a2, self.a3, self.a4)
        self.b4().showMessage('Message in status bar.')
        b2 = QPushButton('Open class2', self)
        b2.setToolTip('This opens a b3')
        b2.move(100, 70)
        b2.clicked.connect(self.openDialog)
        self.show()
    def fonk3(self):
        self.b3 = class2()
        self.b3.exec_()
class class2(QDialog):
    def fonk4(self):
        super().fonk4()
        self.b1 = 'class2'
        self.a1 = 10
        self.a2 = 10
        self.a3 = 320
        self.a4 = 240
        self.fonk5()
    def fonk5(self):
        self.setWindowTitle(self.b1)
        self.setGeometry(self.a1, self.a2, self.a3, self.a4)
        self.b4 = QStatusBar()
        self.fonk7(self.b4)
        self.b4.showMessage('Message in status bar.')
        b2 = QPushButton('PyQt5 Button', self)
        b2.setToolTip('This is an example b2')
        b2.move(100, 70)
        b2.clicked.connect(self.slot_method)
    @pyqtSlot()
    def fonk6(self):
        print('Slot method is called.')
    def fonk7(self, b5):
        self.b5 = b5
        b6 = self.b6() or QVBoxLayout()
        b6.addWidget(b5)
        self.setLayout(b6)
if b7 = = '__main__':
    b8 = QApplication(sys.argv)
    b9 = class1()
    sys.exit(b8.exec_())