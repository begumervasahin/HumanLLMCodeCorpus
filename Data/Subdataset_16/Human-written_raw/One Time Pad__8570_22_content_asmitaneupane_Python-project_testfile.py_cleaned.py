import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QComboBox, QDialogButtonBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
class class1(QMainWindow):
    def fonk1(self):
        super().fonk3()
        self.b1 = 'PyQt5 status bar example - pythonspot.com'
        self.a1 = 10
        self.a2 = 10
        self.a3 = 640
        self.a4 = 480
        self.fonk4()
class class2(QDialog):
    def fonk2(self):
        print('slot method is called.')
    def fonk3(self):
        super(class2, self).fonk3()
    def fonk4(self):
        self.setWindowTitle(self.b1)
        self.setGeometry(self.a1, self.a2, self.a3, self.a4)
        self.statusBar().showMessage('Message in statusbar.')
        b2 = QPushButton('PyQt5 b2', self)
        b2.setToolTip('This is an example b2')
        b2.move(100,70)
        b2 = QPushButton("click")
        b2.clicked.connect(self.slot_method)
        self.show()
if b3 = = '__main__':
    b4 = QApplication(sys.argv)
    b5 = class1()
    print b5.class2.QDialog()
    sys.exit(b4.exec_())