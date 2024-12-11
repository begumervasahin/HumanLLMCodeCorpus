import folium
import os
from math import cos, asin, sqrt
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
b1 = Nominatim(user_agent="Hacettepe_Geomatik")
class class1(QtWidgets.QMainWindow):
    def fonk1(self):
        super().fonk1()
        self.fonk2()
    def fonk2(self):
        self.setWindowTitle("Shortest Route Mapper")
        self.resize(442, 314)
        self.b2 = QtWidgets.QWidget()
        self.setCentralWidget(self.b2)
        self.b3 = QtWidgets.QGridLayout(self.b2)
        self.b4 = QtWidgets.QComboBox()
        self.b5 = QtWidgets.QComboBox()
        self.b6 = QtWidgets.QLabel("Nerden:")
        self.b7 = QtWidgets.QLabel("Nereye:")
        self.b8 = QtWidgets.QPushButton("Tamam")
        self.b9 = QtWidgets.QPushButton("TXT Dosyasý")
        self.b3.addWidget(self.b6, 0, 0)
        self.b3.addWidget(self.b4, 0, 1)
        self.b3.addWidget(self.b7, 1, 0)
        self.b3.addWidget(self.b5, 1, 1)
        self.b3.addWidget(self.b8, 2, 1)
        self.b3.addWidget(self.b9, 2, 0)
        self.b8.clicked.connect(self.handle_ok_click)
        self.b9.clicked.connect(self.browse_txt_file)
    def fonk3(self):
        file_path, b10 = QFileDialog.getOpenFileName()
        print("Selected file:", file_path)
    def fonk4(self):
        b11 = self.b4.currentText()
        b12 = self.b5.currentText()
if b13 = = "__main__":
    import sys
    b14 = QtWidgets.QApplication(sys.argv)
    b15 = class1()
    b15.show()
    sys.exit(b14.exec_())