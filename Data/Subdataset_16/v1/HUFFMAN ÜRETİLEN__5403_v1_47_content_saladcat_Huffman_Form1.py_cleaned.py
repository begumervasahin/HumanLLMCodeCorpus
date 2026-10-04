from PyQt5 import QtCore, QtGui, QtWidgets
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
        b11 = QtWidgets.QTableWidgetItem()
        self.b10.setHorizontalHeaderItem(0, b11)
        b11 = QtWidgets.QTableWidgetItem()
        self.b10.setHorizontalHeaderItem(1, b11)
        self.fonk2(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def fonk2(self, Form):
        b12 = QtCore.QCoreApplication.translate
        Form.setWindowTitle(b12("Form", "Encoding/Decoding Tool"))
        self.b1.setTitle(b12("Form", "Input String for Encoding"))
        self.b2.setText(b12("Form", "Encode"))
        self.b4.setText(b12("Form", "Reset"))
        self.b5.setTitle(b12("Form", "Encoding Table"))
        self.b6.setTitle(b12("Form", "Decode String"))
        self.b8.setText(b12("Form", "Decode"))
        b11 = self.b10.horizontalHeaderItem(0)
        b11.setText(b12("Form", "Key"))
        b11 = self.b10.horizontalHeaderItem(1)
        b11.setText(b12("Form", "Code"))
class class2(QtWidgets.QWidget, class1):
    def fonk3(self):
        super().fonk3()
        self.fonk1(self)
        self.b2.clicked.connect(self.encode_text)
        self.b8.clicked.connect(self.decode_text)
        self.b4.clicked.connect(self.reset_fields)
        self.b13 = {}
    def fonk4(self):
        b14 = self.b3.toPlainText()
        if b14:
            self.b13 = self.fonk8(b14)
            self.fonk7()
            b15 = ''.join(self.b13[char] for char in b14 if char in self.b13)
            self.b7.setPlainText(b15)
    def fonk5(self):
        b15 = self.b7.toPlainText()
        if b15:
            b16 = {v: k for k, v in self.b13.items()}
            b17 = ""
            b18 = ""
            for bit in b15:
                b18 += bit
                if b18 in b16:
                    b17 += b16[b18]
                    b18 = ""
            self.b9.setPlainText(b17)
    def fonk6(self):
        self.b3.clear()
        self.b7.clear()
        self.b9.clear()
        self.b10.setRowCount(0)
        self.b13.clear()
    def fonk7(self):
        self.b10.setRowCount(0)
        for key, code in self.b13.items():
            b19 = self.b10.rowCount()
            self.b10.insertRow(b19)
            self.b10.setItem(b19, 0, QtWidgets.QTableWidgetItem(key))
            self.b10.setItem(b19, 1, QtWidgets.QTableWidgetItem(code))
    def fonk8(self, b14):
        b20 = defaultdict(int)
        for char in b14:
            b20[char] += 1
        b21 = sorted(b20.items(), key=lambda b11: b11[1], reverse=True)
        b22 = {char: bin(i)[2:].zfill(5) for i, (char, _) in enumerate(b21)}
        return b22
if b23 = = "__main__":
    import sys
    b24 = QtWidgets.QApplication(sys.argv)
    b25 = class2()
    b25.show()
    sys.exit(b24.exec_())