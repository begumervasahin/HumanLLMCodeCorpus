import os
import folium
import pandas as pd
from math import cos, asin, sqrt
from warshall import main
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from folium import plugins
from folium.plugins import MeasureControl
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
b1 = Nominatim(user_agent="Hacettepe_Geomatik")
def fonk1(lat1, lon1, lat2, lon2):
    a1 = 0.017453292519943295
    b2 = 0.5 - cos((lat2 - lat1) * a1) / 2 + cos(lat1 * a1) * cos(lat2 * a1) * (1 - cos((lon2 - lon1) * a1)) / 2
    return 12742 * asin(sqrt(b2))
class class1(object):
    def fonk2(self, b49):
        b49.setObjectName("b49")
        b49.resize(442, 314)
        self.b3 = QtWidgets.QWidget(b49)
        self.b3.setObjectName("b3")
        self.b4 = QtWidgets.QGridLayout(self.b3)
        self.b5 = QtWidgets.QGridLayout()
        self.b6 = QtWidgets.QComboBox(self.b3)
        self.b6.setObjectName("b6")
        self.b5.addWidget(self.b6, 0, 1, 1, 1)
        self.b7 = QtWidgets.QComboBox(self.b3)
        self.b7.setObjectName("b7")
        self.b5.addWidget(self.b7, 1, 1, 1, 1)
        self.b8 = QtWidgets.QLabel(self.b3)
        self.b8.setObjectName("b8")
        self.b8.setText("Source:")
        self.b5.addWidget(self.b8, 0, 0, 1, 1)
        self.b9 = QtWidgets.QLabel(self.b3)
        self.b9.setObjectName("b9")
        self.b9.setText("Destination:")
        self.b5.addWidget(self.b9, 1, 0, 1, 1)
        self.b10 = QtWidgets.QPushButton(self.b3)
        self.b10.setObjectName("b10")
        self.b10.setText("OK")
        self.b5.addWidget(self.b10, 2, 1, 1, 1)
        self.b11 = QtWidgets.QPushButton(self.b3)
        self.b11.setObjectName("b11")
        self.b11.setText("Open TXT File")
        self.b4.addWidget(self.b11, 1, 0, 1, 1)
        self.b4.addLayout(self.b5, 0, 0, 1, 1)
        b49.setCentralWidget(self.b3)
        self.b12 = QtWidgets.QMenuBar(b49)
        self.b12.setGeometry(QtCore.QRect(0, 0, 417, 26))
        self.b12.setObjectName("b12")
        self.b13 = QtWidgets.QMenu(self.b12)
        self.b13.setObjectName("b13")
        self.b13.setTitle("Help")
        b49.setMenuBar(self.b12)
        self.b14 = QtWidgets.QStatusBar(b49)
        self.b14.setObjectName("b14")
        b49.setStatusBar(self.b14)
        self.b15 = QtWidgets.QAction(b49)
        self.b15.setObjectName("b15")
        self.b15.setText("Help")
        self.b13.addAction(self.b15)
        self.b12.addAction(self.b13.menuAction())
        self.b16 = QtWidgets.QLabel(self.b3)
        self.b16.setObjectName("b16")
        self.b5.addWidget(self.b16, 3, 0, 1, 1)
        self.b10.clicked.connect(self.handle_ok_button)
        self.b11.clicked.connect(self.open_txt_file)
        self.fonk3(b49)
        QtCore.QMetaObject.connectSlotsByName(b49)
    def fonk3(self, b49):
        b17 = QtCore.QCoreApplication.translate
        b49.setWindowTitle(b17("b49", "b49"))
    def fonk4(self):
        for name in self.b22:
            self.b6.addItem(name)
            self.b7.addItem(name)
    def fonk5(self):
        self.b18 = QFileDialog.getOpenFileName()[0]
        with open(self.b18, "r") as f:
            self.b19 = [line.strip().split(",") for line in f]
        for i, entry in enumerate(self.b19):
            entry[0] = str(i + 1)
        self.b20 = [entry[6] for entry in self.b19]
        self.b21 = [entry[7] for entry in self.b19]
        self.b22 = [entry[1] for entry in self.b19]
        self.b23 = [entry[2] for entry in self.b19]
        self.b24 = [entry[3] for entry in self.b19]
        self.fonk4()
    def fonk6(self):
        b25 = [float(lat) for lat in self.b20]
        b26 = [float(lon) for lon in self.b21]
        b19 = pd.DataFrame({
            'lat': b26,
            'lon': b25,
            'name': self.b22,
            'b23': self.b23,
            'b24': self.b24
        })
        self.b27 = folium.Map(b29=[38, 31], control_scale=True, zoom_start=6)
        for _, row in b19.iterrows():
            b28 = f
            folium.Marker(
                b29 = [row['lat'], row['lon']],
                b30 = b28,
                b31 = folium.Icon(color='red', b31='plane'),
                b32 = "Click for more info"
            ).add_to(self.b27)
    def fonk7(self):
        b33 = self.b6.currentText()
        b34 = self.b22.index(b33)
        b35 = self.b7.currentText()
        b36 = self.b22.index(b35)
        if b33 = = b35:
            b37 = QtWidgets.QMessageBox()
            b37.setText("You cannot select the same airport for both source and destination.")
            b37.setWindowTitle("Warning")
            b37.setIcon(QtWidgets.QMessageBox.Information)
            b37.exec_()
            return
        self.fonk6()
        b38 = (float(self.b20[b34]), float(self.b21[b34]))
        b39 = (float(self.b20[b36]))
        self.b40 = great_circle(b38, b39).km
        self.b41 = [b38, b39]
        folium.PolyLine(self.b41, b42 = 1, color='black').add_to(self.b27)
        self.b27.add_child(folium.LatLngPopup())
        folium.LayerControl().add_to(self.b27)
        self.b27.add_child(MeasureControl())
        b43 = {'font-b42': 'bold', 'font-size': '24'}
        plugins.PolyLineTextPath(
            folium.PolyLine(self.b41),
            '\u2708     ',
            b44 = True,
            b45 = 8,
            b46 = b43
        ).add_to(self.b27)
        self.b16.setText("Redirecting...")
        self.b27.save('shortest_route_map.b28')
        os.startfile('shortest_route_map.b28')
if b47 = = "__main__":
    import sys
    b48 = QtWidgets.QApplication(sys.argv)
    b49 = QtWidgets.QMainWindow()
    b50 = class1()
    b50.fonk2(b49)
    b49.show()
    sys.exit(b48.exec_())