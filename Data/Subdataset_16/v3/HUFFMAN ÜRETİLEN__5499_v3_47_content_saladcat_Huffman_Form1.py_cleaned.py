import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from collections import defaultdict
class class1(object):
    def fonk1(self, Form):
        Form.setObjectName("Form")
        Form.resize(1069, 719)
        self.b1 = QtWidgets.QGroupBox(Form)
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
        self.b5 = QtWidgets.QGroupBox(Form)
        self.b5.setGeometry(QtCore.QRect(340, 40, 681, 641))
        self.b5.setObjectName("b5")
        self.b6 = QtWidgets.QGroupBox(Form)
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
        self.b10.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("Key"))
        self.b10.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Code"))
        self.fonk2(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def fonk2(self, Form):
        b11 = QtCore.QCoreApplication.translate
        Form.setWindowTitle(b11("Form", "Encoding/Decoding Tool"))
        self.b1.setTitle(b11("Form", "Input String for Encoding"))
        self.b2.setText(b11("Form", "Encode"))
        self.b4.setText(b11("Form", "Reset"))
        self.b5.setTitle(b11("Form", "Encoding Table"))
        self.b6.setTitle(b11("Form", "Decode String"))
        self.b8.setText(b11("Form", "Decode"))
class class2(QtWidgets.QWidget, class1):
    def fonk3(self):
        super().fonk3()
        self.fonk1(self)
        self.b12 = {}
        self.b2.clicked.connect(self.encode_text)
        self.b8.clicked.connect(self.decode_text)
        self.b4.clicked.connect(self.reset_fields)
    def fonk4(self):
        b13 = self.b3.toPlainText()
        if b13:
            self.b12 = self.fonk8(b13)
            self.fonk7()
            b14 = ''.join(self.b12[char] for char in b13 if char in self.b12)
            self.b7.setPlainText(b14)
    def fonk5(self):
        b14 = self.b7.toPlainText()
        if b14:
            b15 = self.fonk9(b14)
            self.b9.setPlainText(b15)
    def fonk6(self):
        self.b3.clear()
        self.b7.clear()
        self.b9.clear()
        self.b10.setRowCount(0)
        self.b12.clear()
    def fonk7(self):
        self.b10.setRowCount(0)
        for key, code in self.b12.items():
            b16 = self.b10.rowCount()
            self.b10.insertRow(b16)
            self.b10.setItem(b16, 0, QtWidgets.QTableWidgetItem(key))
            self.b10.setItem(b16, 1, QtWidgets.QTableWidgetItem(code))
    def fonk8(self, b13):
        b17 = defaultdict(int)
        for char in b13:
            b17[char] += 1
        b18 = sorted(b17.items(), key=lambda item: item[1], reverse=True)
        b19 = {char: bin(i)[2:].zfill(5) for i, (char, _) in enumerate(b18)}
        return b19
    def fonk9(self, b14):
        b20 = {v: k for k, v in self.b12.items()}
        b15 = ""
        b21 = ""
        for bit in b14:
            b21 += bit
            if b21 in b20:
                b15 += b20[b21]
                b21 = ""
        return b15
if b22 = = "__main__":
    b23 = QtWidgets.QApplication(sys.argv)
    b24 = class2()
    b24.show()
    sys.exit(b23.exec_())