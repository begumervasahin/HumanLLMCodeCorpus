import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QDialog, QMessageBox
class class1(QMainWindow):
    def fonk1(self):
        super().fonk4()
        self.fonk2()
    def fonk2(self):
        self.setWindowTitle('PyQt5 Status Bar Example')
        self.setGeometry(10, 10, 640, 480)
        self.statusBar().showMessage('Message in status bar.')
        b1 = QPushButton('Open Dialog', self)
        b1.setToolTip('This is an example b1')
        b1.move(100, 70)
        b1.clicked.connect(self.openDialog)
    def fonk3(self):
        b2 = class2()
        b2.exec_()
class class2(QDialog):
    def fonk4(self):
        super().fonk4()
        self.setWindowTitle('Custom Dialog')
        self.setGeometry(100, 100, 200, 100)
        b1 = QPushButton('Click me', self)
        b1.move(50, 30)
        b1.clicked.connect(self.slot_method)
    def fonk5(self):
        QMessageBox.information(self, 'Information', 'Slot method is called.')
if b3 = = '__main__':
    b4 = QApplication(sys.argv)
    b5 = class1()
    b5.show()
    sys.exit(b4.exec_())