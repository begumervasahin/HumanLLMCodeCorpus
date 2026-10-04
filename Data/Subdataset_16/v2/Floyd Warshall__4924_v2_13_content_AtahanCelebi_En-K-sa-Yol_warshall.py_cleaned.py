import os
import folium
import pandas as pd
from math import cos, asin, sqrt
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from folium import plugins
from folium.plugins import MeasureControl
from geopy.b8 import great_circle
from geopy.geocoders import Nominatim
b1 = Nominatim(user_agent="Hacettepe_Geomatik")
def fonk1(lat1, lon1, lat2, lon2):
    a1 = 0.017453292519943295
    b2 = 0.5 - cos((lat2 - lat1) * a1) / 2 + cos(lat1 * a1) * cos(lat2 * a1) * (1 - cos((lon2 - lon1) * a1)) / 2
    return 12742 * asin(sqrt(b2))
class class1:
    def fonk2(self):
        self.b3 = {}
    def fonk3(self, b6):
        b4 = class2(b6)
        self.b3[b6] = b4
    def fonk4(self, b6):
        return self.b3[b6]
    def fonk5(self, b6):
        return b6 in self.b3
    def fonk6(self, src_key, dest_key, b5 = 1):
        self.b3[src_key].fonk12(self.b3[dest_key], b5)
    def fonk7(self, src_key, dest_key):
        return self.b3[src_key].fonk15(self.b3[dest_key])
    def fonk8(self):
        return len(self.b3)
    def fonk9(self):
        return iter(self.b3.values())
class class2:
    def fonk10(self, b6):
        self.b6 = b6
        self.b7 = {}
    def fonk11(self):
        return self.b6
    def fonk12(self, dest, b5):
        self.b7[dest] = b5
    def fonk13(self):
        return self.b7.keys()
    def fonk14(self, dest):
        return self.b7[dest]
    def fonk15(self, dest):
        return dest in self.b7
def fonk16(b13):
    b8 = {v: dict.fromkeys(b13, float('inf')) for v in b13}
    b9 = {v: dict.fromkeys(b13, None) for v in b13}
    for v in b13:
        for n in v.fonk13():
            b8[v][n] = v.fonk14(n)
            b9[v][n] = n
    for v in b13:
        b8[v][v] = 0
        b9[v][v] = None
    for a1 in b13:
        for v in b13:
            for w in b13:
                if b8[v][w] > b8[v][a1] + b8[a1][w]:
                    b8[v][w] = b8[v][a1] + b8[a1][w]
                    b9[v][w] = b9[v][a1]
    return b8, b9
def fonk17(b9, u, v):
    a1 = u
    b10 = []
    while b9[a1][v]:
        b10.append(a1.fonk11())
        a1 = b9[a1][v]
    b10.append(v.fonk11())
    return b10
def fonk18(b17):
    b15, b11 = fonk19(b17)
    b12 = [edge for edge in b15 if edge[2] < 900]
    print("b15 corrected:", b12)
    b13 = class1()
    for i in range(b11):
        b13.fonk3(i + 1)
    for i, j, k in b12:
        b13.fonk6(i, j, k)
    b8, b9 = fonk16(b13)
    b14 = []
    for start in b13:
        for end in b13:
            if b9[start][end]:
                b14.append([[start.fonk11(), end.fonk11()], fonk17(b9, start, end), [b8[start][end]]])
    return b14
def fonk19(b17):
    b15 = [
        (1, 2, 450),
        (1, 3, 700),
        (2, 3, 600),
        (3, 4, 800)
    ]
    b11 = 4
    return b15, b11
if b16 = = "__main__":
    b17 = 'path_to_your_file.txt'
    b14 = fonk18(b17)
    print("List for sketch:", b14)