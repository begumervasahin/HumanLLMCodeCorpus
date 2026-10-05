from PyQt5 import QtCore, QtGui, QtWidgets
class class1(object):
    def fonk1(self, b16):
        b16.setObjectName("b16")
        b16.resize(1069, 719)
        self.fonk2(b16)
        self.fonk3(b16)
        self.fonk4(b16)
        self.fonk6(b16)
        QtCore.QMetaObject.connectSlotsByName(b16)
    def fonk2(self, b16):
        self.b1 = QtWidgets.QGroupBox(b16)
        self.b1.setGeometry(QtCore.QRect(20, 30, 311, 181))
        self.b1.setObjectName("b1")
        self.b2 = QtWidgets.QPushButton(self.b1)
        self.b2.setGeometry(QtCore.QRect(180, 50, 113, 32))
        self.b2.setObjectName("b2")
        self.b3 = QtWidgets.QPlainTextEdit(self.b1)
        self.b3.setGeometry(QtCore.QRect(10, 30, 171, 141))
        self.b3.setObjectName("b3")
        self.b4 = QtWidgets.QPushButton(self.b1)
        self.b4.setGeometry(QtCore.QRect(180, 120, 113, 32))
        self.b4.setObjectName("b4")
    def fonk3(self, b16):
        self.b5 = QtWidgets.QGroupBox(b16)
        self.b5.setGeometry(QtCore.QRect(340, 40, 681, 641))
        self.b5.setObjectName("b5")
    def fonk4(self, b16):
        self.b6 = QtWidgets.QGroupBox(b16)
        self.b6.setGeometry(QtCore.QRect(20, 220, 311, 471))
        self.b6.setObjectName("b6")
        self.b7 = QtWidgets.QPlainTextEdit(self.b6)
        self.b7.setGeometry(QtCore.QRect(10, 40, 281, 41))
        self.b7.setObjectName("b7")
        self.b8 = QtWidgets.QPushButton(self.b6)
        self.b8.setGeometry(QtCore.QRect(90, 100, 113, 32))
        self.b8.setObjectName("b8")
        self.b9 = QtWidgets.QPlainTextEdit(self.b6)
        self.b9.setGeometry(QtCore.QRect(10, 140, 281, 51))
        self.b9.setObjectName("b9")
        self.b10 = QtWidgets.QTableWidget(self.b6)
        self.b10.setGeometry(QtCore.QRect(40, 210, 211, 241))
        self.b10.setObjectName("b10")
        self.b10.setColumnCount(2)
        self.b10.setRowCount(0)
        self.fonk5()
    def fonk5(self):
        b11 = ["Key", "Code"]
        for i, label in enumerate(b11):
            b12 = QtWidgets.QTableWidgetItem()
            b12.setText(label)
            self.b10.setHorizontalHeaderItem(i, b12)
    def fonk6(self, b16):
        b13 = QtCore.QCoreApplication.translate
        b16.setWindowTitle(b13("b16", "b16"))
        self.b1.setTitle(b13("b16", "Init Encode String"))
        self.b2.setText(b13("b16", "Encode"))
        self.b4.setText(b13("b16", "Reset"))
        self.b5.setTitle(b13("b16", "Encode Table"))
        self.b6.setTitle(b13("b16", "Decode String"))
        self.b8.setText(b13("b16", "PushButton"))
if b14 = = "__main__":
    import sys
    b15 = QtWidgets.QApplication(sys.argv)
    b16 = QtWidgets.QWidget()
    b17 = class1()
    b17.fonk1(b16)
    b16.show()
    sys.exit(b15.exec_())