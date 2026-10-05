import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QDialog, QMessageBox
class class1(QMainWindow):
    def fonk1(self):
        super().fonk4()
        self.b1 = 'PyQt5 Status Bar Example'
        self.a1 = 10
        self.a2 = 10
        self.a3 = 640
        self.a4 = 480
        self.fonk2()
    def fonk2(self):
        self.setWindowTitle(self.b1)
        self.setGeometry(self.a1, self.a2, self.a3, self.a4)
        self.statusBar().showMessage('Message in status bar.')
        b2 = QPushButton('Open Dialog', self)
        b2.setToolTip('This is an example b2')
        b2.move(100, 70)
        b2.clicked.connect(self.openDialog)
        self.show()
    def fonk3(self):
        b3 = class2()
        b3.exec_()
class class2(QDialog):
    def fonk4(self):
        super().fonk4()
        self.setWindowTitle('Custom Dialog')
        self.setGeometry(100, 100, 200, 100)
        b2 = QPushButton('Click me', self)
        b2.move(50, 30)
        b2.clicked.connect(self.slot_method)
    def fonk5(self):
        QMessageBox.information(self, 'Information', 'Slot method is called.')
if b4 = = '__main__':
    b5 = QApplication(sys.argv)
    b6 = class1()
    sys.exit(b5.exec_())