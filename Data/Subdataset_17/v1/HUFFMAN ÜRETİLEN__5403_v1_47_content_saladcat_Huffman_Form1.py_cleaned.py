from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1069, 719)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 311, 181))
        self.groupBox.setObjectName("groupBox")
        self.pb_encode = QtWidgets.QPushButton(self.groupBox)
        self.pb_encode.setGeometry(QtCore.QRect(180, 50, 113, 32))
        self.pb_encode.setObjectName("pb_encode")
        self.pte_encode = QtWidgets.QPlainTextEdit(self.groupBox)
        self.pte_encode.setGeometry(QtCore.QRect(10, 30, 171, 141))
        self.pte_encode.setObjectName("pte_encode")
        self.pb_reset = QtWidgets.QPushButton(self.groupBox)
        self.pb_reset.setGeometry(QtCore.QRect(180, 120, 113, 32))
        self.pb_reset.setObjectName("pb_reset")
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(340, 40, 681, 641))
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 220, 311, 471))
        self.groupBox_3.setObjectName("groupBox_3")
        self.pte_decode_input = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.pte_decode_input.setGeometry(QtCore.QRect(10, 40, 281, 41))
        self.pte_decode_input.setObjectName("pte_decode_input")
        self.pb_decode = QtWidgets.QPushButton(self.groupBox_3)
        self.pb_decode.setGeometry(QtCore.QRect(90, 100, 113, 32))
        self.pb_decode.setObjectName("pb_decode")
        self.pte_decode_output = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.pte_decode_output.setGeometry(QtCore.QRect(10, 140, 281, 51))
        self.pte_decode_output.setObjectName("pte_decode_output")
        self.tw_encode_table = QtWidgets.QTableWidget(self.groupBox_3)
        self.tw_encode_table.setGeometry(QtCore.QRect(40, 210, 211, 241))
        self.tw_encode_table.setObjectName("tw_encode_table")
        self.tw_encode_table.setColumnCount(2)
        self.tw_encode_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tw_encode_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_encode_table.setHorizontalHeaderItem(1, item)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Encoding/Decoding Tool"))
        self.groupBox.setTitle(_translate("Form", "Input String for Encoding"))
        self.pb_encode.setText(_translate("Form", "Encode"))
        self.pb_reset.setText(_translate("Form", "Reset"))
        self.groupBox_4.setTitle(_translate("Form", "Encoding Table"))
        self.groupBox_3.setTitle(_translate("Form", "Decode String"))
        self.pb_decode.setText(_translate("Form", "Decode"))
        item = self.tw_encode_table.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Key"))
        item = self.tw_encode_table.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Code"))
class MyApp(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb_encode.clicked.connect(self.encode_text)
        self.pb_decode.clicked.connect(self.decode_text)
        self.pb_reset.clicked.connect(self.reset_fields)
        self.encoding_map = {}
    def encode_text(self):
        text = self.pte_encode.toPlainText()
        if text:
            self.encoding_map = self.generate_huffman_codes(text)
            self.populate_encode_table()
            encoded_text = ''.join(self.encoding_map[char] for char in text if char in self.encoding_map)
            self.pte_decode_input.setPlainText(encoded_text)
    def decode_text(self):
        encoded_text = self.pte_decode_input.toPlainText()
        if encoded_text:
            reversed_map = {v: k for k, v in self.encoding_map.items()}
            decoded_text = ""
            buffer = ""
            for bit in encoded_text:
                buffer += bit
                if buffer in reversed_map:
                    decoded_text += reversed_map[buffer]
                    buffer = ""
            self.pte_decode_output.setPlainText(decoded_text)
    def reset_fields(self):
        self.pte_encode.clear()
        self.pte_decode_input.clear()
        self.pte_decode_output.clear()
        self.tw_encode_table.setRowCount(0)
        self.encoding_map.clear()
    def populate_encode_table(self):
        self.tw_encode_table.setRowCount(0)
        for key, code in self.encoding_map.items():
            row_position = self.tw_encode_table.rowCount()
            self.tw_encode_table.insertRow(row_position)
            self.tw_encode_table.setItem(row_position, 0, QtWidgets.QTableWidgetItem(key))
            self.tw_encode_table.setItem(row_position, 1, QtWidgets.QTableWidgetItem(code))
    def generate_huffman_codes(self, text):
        frequency = defaultdict(int)
        for char in text:
            frequency[char] += 1
        sorted_chars = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
        codes = {char: bin(i)[2:].zfill(5) for i, (char, _) in enumerate(sorted_chars)}
        return codes
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())