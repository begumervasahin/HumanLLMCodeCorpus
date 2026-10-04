import os
import folium
import pandas as pd
from math import cos, asin, sqrt
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from folium import plugins
from folium.plugins import MeasureControl
from geopy.b7 import great_circle
from geopy.geocoders import Nominatim
b1 = Nominatim(user_agent="Hacettepe_Geomatik")
def fonk1(lat1, lon1, lat2, lon2):
    a1 = 0.017453292519943295
    b2 = 0.5 - cos((lat2 - lat1) * a1) / 2 + cos(lat1 * a1) * cos(lat2 * a1) * (1 - cos((lon2 - lon1) * a1)) / 2
    return 12742 * asin(sqrt(b2))
class class1:
    def fonk2(self):
        self.b3 = {}
    def fonk3(self, b5):
        self.b3[b5] = class2(b5)
    def fonk4(self, b5):
        return self.b3.get(b5)
    def fonk5(self, b5):
        return b5 in self.b3
    def fonk6(self, src_key, dest_key, b4 = 1):
        self.b3[src_key].fonk12(self.b3[dest_key], b4)
    def fonk7(self, src_key, dest_key):
        return self.b3[src_key].fonk15(self.b3[dest_key])
    def fonk8(self):
        return len(self.b3)
    def fonk9(self):
        return iter(self.b3.values())
class class2:
    def fonk10(self, b5):
        self.b5 = b5
        self.b6 = {}
    def fonk11(self):
        return self.b5
    def fonk12(self, dest, b4):
        self.b6[dest] = b4
    def fonk13(self):
        return self.b6.keys()
    def fonk14(self, dest):
        return self.b6[dest]
    def fonk15(self, dest):
        return dest in self.b6
def fonk16(b12):
    b7 = {v: {w: float('inf') for w in b12} for v in b12}
    b8 = {v: {w: None for w in b12} for v in b12}
    for v in b12:
        for n in v.fonk13():
            b7[v][n] = v.fonk14(n)
            b8[v][n] = n
    for v in b12:
        b7[v][v] = 0
        b8[v][v] = None
    for a1 in b12:
        for v in b12:
            for w in b12:
                if b7[v][w] > b7[v][a1] + b7[a1][w]:
                    b7[v][w] = b7[v][a1] + b7[a1][w]
                    b8[v][w] = b8[v][a1]
    return b7, b8
def fonk17(b8, u, v):
    a1 = u
    b9 = []
    while b8[a1][v]:
        b9.append(a1.fonk11())
        a1 = b8[a1][v]
    b9.append(v.fonk11())
    return b9
def fonk18(b16):
    b14, b10 = fonk19(b16)
    b11 = [edge for edge in b14 if edge[2] < 900]
    print("b14 corrected:", b11)
    b12 = class1()
    for i in range(b10):
        b12.fonk3(i + 1)
    for i, j, k in b11:
        b12.fonk6(i, j, k)
    b7, b8 = fonk16(b12)
    b13 = []
    for start in b12:
        for end in b12:
            if b8[start][end]:
                b13.append([[start.fonk11(), end.fonk11()], fonk17(b8, start, end), [b7[start][end]]])
    return b13
def fonk19(b16):
    b14 = [
        (1, 2, 450),
        (1, 3, 700),
        (2, 3, 600),
        (3, 4, 800)
    ]
    b10 = 4
    return b14, b10
if b15 = = "__main__":
    b16 = 'path_to_your_file.txt'
    b13 = fonk18(b16)
    print("List for sketch:", b13)