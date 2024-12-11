import folium
import os
from math import cos, asin, sqrt
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import pandas as pd
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
from folium import plugins
from folium.plugins import MeasureControl
from warshall import main
b1 = Nominatim(user_agent="Hacettepe_Geomatik")
def fonk1(lat1, lon1, lat2, lon2):
    a1 = 0.017453292519943295
    b2 = 0.5 - cos((lat2 - lat1) * a1) / 2 + cos(lat1 * a1) * cos(lat2 * a1) * (1 - cos((lon2 - lon1) * a1)) / 2
    return 12742 * asin(sqrt(b2))
class class1(QtWidgets.QMainWindow):
    def fonk2(self):
        super().fonk2()
        self.fonk3()
    def fonk3(self):
        self.setWindowTitle("Shortest Route Mapper")
        self.resize(442, 314)
        self.b3 = QtWidgets.QWidget()
        self.setCentralWidget(self.b3)
        self.b4 = QtWidgets.QGridLayout(self.b3)
        self.b5 = QtWidgets.QComboBox()
        self.b6 = QtWidgets.QComboBox()
        self.b7 = QtWidgets.QLabel("Nerden:")
        self.b8 = QtWidgets.QLabel("Nereye:")
        self.b9 = QtWidgets.QPushButton("Tamam")
        self.b10 = QtWidgets.QPushButton("TXT Dosyasý")
        self.b4.addWidget(self.b7, 0, 0)
        self.b4.addWidget(self.b5, 0, 1)
        self.b4.addWidget(self.b8, 1, 0)
        self.b4.addWidget(self.b6, 1, 1)
        self.b4.addWidget(self.b9, 2, 1)
        self.b4.addWidget(self.b10, 2, 0)
        self.b9.clicked.connect(self.handle_ok_click)
        self.b10.clicked.connect(self.browse_txt_file)
    def fonk4(self):
        file_path, b11 = QFileDialog.getOpenFileName()
        print("Selected file:", file_path)
    def fonk5(self):
        b12 = self.b5.currentText()
        b13 = self.b6.currentText()
if b14 = = "__main__":
    import sys
    b15 = QtWidgets.QApplication(sys.argv)
    b16 = class1()
    b16.show()
    sys.exit(b15.exec_())