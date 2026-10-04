import os
import folium
import pandas as pd
from math import cos, asin, sqrt
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from folium import plugins
from folium.plugins import MeasureControl
b1 = Nominatim(user_agent="Hacettepe_Geomatik")
def fonk1(lat1, lon1, lat2, lon2):
    a1 = 0.017453292519943295
    b2 = 0.5 - cos((lat2 - lat1) * a1) / 2 + cos(lat1 * a1) * cos(lat2 * a1) * (1 - cos((lon2 - lon1) * a1)) / 2
    return 12742 * asin(sqrt(b2))
class class1(object):
    def fonk2(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(442, 314)
        self.b3 = QtWidgets.QWidget(MainWindow)
        self.b3.setObjectName("b3")
        self.b4 = QtWidgets.QGridLayout(self.b3)
        self.b4.setObjectName("b4")
        self.b5 = QtWidgets.QGridLayout()
        self.b5.setObjectName("b5")
        self.b6 = QtWidgets.QComboBox(self.b3)
        self.b6.setObjectName("b6")
        self.b5.addWidget(self.b6, 1, 1, 1, 1)
        self.b7 = QtWidgets.QLabel(self.b3)
        self.b7.setObjectName("b7")
        self.b5.addWidget(self.b7, 1, 0, 1, 1)
        self.b8 = QtWidgets.QLabel(self.b3)
        self.b8.setObjectName("b8")
        self.b5.addWidget(self.b8, 0, 0, 1, 1)
        self.b9 = QtWidgets.QComboBox(self.b3)
        self.b9.setObjectName("b9")
        self.b5.addWidget(self.b9, 0, 1, 1, 1)
        self.b10 = QtWidgets.QPushButton(self.b3)
        self.b10.setObjectName("b10")
        self.b5.addWidget(self.b10, 2, 1, 1, 1)
        self.b4.addLayout(self.b5, 0, 0, 1, 1)
        self.b11 = QtWidgets.QPushButton(self.b3)
        self.b11.setObjectName("b11")
        self.b4.addWidget(self.b11, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.b3)
        self.b12 = QtWidgets.QMenuBar(MainWindow)
        self.b12.setGeometry(QtCore.QRect(0, 0, 417, 26))
        self.b12.setObjectName("b12")
        self.b13 = QtWidgets.QMenu(self.b12)
        self.b13.setObjectName("b13")
        MainWindow.setMenuBar(self.b12)
        self.b14 = QtWidgets.QStatusBar(MainWindow)
        self.b14.setObjectName("b14")
        MainWindow.setStatusBar(self.b14)
        self.b15 = QtWidgets.QAction(MainWindow)
        self.b15.setObjectName("b15")
        self.b13.addAction(self.b15)
        self.b12.addAction(self.b13.menuAction())
        self.b16 = QtWidgets.QLabel(self.b3)
        self.b16.setObjectName("b16")
        self.b5.addWidget(self.b16, 3, 0, 1, 1)
        self.b10.clicked.connect(self.tamam)
        self.b11.clicked.connect(self.txt_ac)
        self.fonk3(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def fonk3(self, MainWindow):
        b17 = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(b17("MainWindow", "MainWindow"))
        self.b7.setText(b17("MainWindow", "Destination:"))
        self.b8.setText(b17("MainWindow", "Source:"))
        self.b10.setText(b17("MainWindow", "OK"))
        self.b11.setText(b17("MainWindow", "Open TXT File"))
        self.b13.setTitle(b17("MainWindow", "Help"))
        self.b15.setText(b17("MainWindow", "Help"))
    def fonk4(self):
        for i in self.b23:
            self.b9.addItem(i)
            self.b6.addItem(i)
    def fonk5(self):
        self.b18 = QFileDialog.getOpenFileName()
        b19 = open("%s" % (self.b18[0]), "r")
        self.b20 = []
        for i in b19.readlines():
            self.b20.append(i.split(","))
        for i in range(len(self.b20)):
            self.b20[i][0] = str(i + 1)
        self.b21 = list()
        self.b22 = list()
        self.b23 = list()
        self.b24 = list()
        self.b25 = list()
        for i in range(len(self.b20)):
            self.b21.append(self.b20[i][6])
            self.b22.append(self.b20[i][7])
            self.b23.append(self.b20[i][1])
            self.b24.append(self.b20[i][2])
            self.b25.append(self.b20[i][3])
        self.fonk4()
    def fonk6(self):
        b26 = [float(i) for i in self.b21]
        b27 = [float(i) for i in self.b22]
        b20 = pd.DataFrame({
            'lat': b27,
            'lon': b26,
            'b41': self.b23,
            'b24': self.b24,
            'b25': self.b25
        })
        for i in range(len(self.b49)):
            b28 = b19
            folium.Marker(
                b29 = self.b49[i],
                b30 = b28,
                b31 = folium.Icon(b52='red', b31='plane'),
                b32 = "Click for more info"
            ).add_to(self.b38)
    def fonk7(self):
        self.b33 = self.b9.currentText()
        b34 = self.b23.index(self.b33)
        self.b35 = self.b6.currentText()
        b36 = self.b23.index(self.b35)
        if self.b33 = = self.b35:
            b37 = QtWidgets.QMessageBox()
            b37.setText("You cannot select the same airport for both source and destination.")
            b37.setWindowTitle("Warning")
            b37.setIcon(QtWidgets.QMessageBox.Information)
            b37.exec_()
            return
        self.b38 = folium.Map(b29=[38, 31], control_scale=True, zoom_start=6)
        self.b38.add_child(folium.LatLngPopup())
        folium.raster_layers.TileLayer(
            b39 = 'http:
            b40 = 'google',
            b41 = 'google maps',
            b42 = 20,
            b43 = ['mt0', 'mt1', 'mt2', 'mt3'],
            b44 = False,
            b45 = True,
        ).add_to(self.b38)
        folium.raster_layers.TileLayer(
            b39 = 'http:
            b40 = 'google',
            b41 = 'google street view',
            b42 = 20,
            b43 = ['mt0', 'mt1', 'mt2', 'mt3'],
            b44 = False,
            b45 = True,
        ).add_to(self.b38)
        folium.LayerControl().add_to(self.b38)
        self.b38.add_child(MeasureControl())
        b46 = int(self.b20[b34][0])
        b47 = int(self.b20[b36][0])
        self.b48 = great_circle((self.b21[b34], self.b22[b34]), (self.b21[b36], self.b22[b36])).km
        self.b49 = [[self.b21[b34], self.b22[b34]], [self.b21[b36], self.b22[b36]]]
        self.fonk6()
        b50 = folium.PolyLine(
            self.b49,
            b51 = 1,
            b52 = 'black'
        ).add_to(self.b38)
        b40 = {'font-b51': 'bold', 'font-size': '24'}
        plugins.PolyLineTextPath(
            b50,
            '\u2708     ',
            b53 = True,
            b54 = 8,
            b55 = b40
        ).add_to(self.b38)
        self.b16.setText("Redirecting...")
        self.b38.save('shortest_route_map.b28')
        os.b46