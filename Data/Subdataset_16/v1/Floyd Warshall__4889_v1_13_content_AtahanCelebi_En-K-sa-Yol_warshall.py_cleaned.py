import os
from math import cos, asin, sqrt
import folium
import pandas as pd
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from folium import plugins
from folium.plugins import MeasureControl
from geopy.b11 import great_circle
from geopy.geocoders import Nominatim
b1 = Nominatim(user_agent="Hacettepe_Geomatik")
def fonk1(lat1, lon1, lat2, lon2):
    a1 = 0.017453292519943295
    b2 = 0.5 - cos((lat2 - lat1) * a1) / 2 + cos(lat1 * a1) * cos(lat2 * a1) * (1 - cos((lon2 - lon1) * a1)) / 2
    return 12742 * asin(sqrt(b2))
def fonk2(b17):
    b3 = fonk19(b17)[0]
    b4 = [edge for edge in b3 if edge[2] < 900]
    print("b3 corrected:", b4)
    b5 = fonk19(b17)[1]
    class class1:
        def fonk3(self):
            self.b6 = {}
        def fonk4(self, b9):
            b7 = class2(b9)
            self.b6[b9] = b7
        def fonk5(self, b9):
            return self.b6[b9]
        def fonk6(self, b9):
            return b9 in self.b6
        def fonk7(self, src_key, dest_key, b8 = 1):
            self.b6[src_key].fonk13(self.b6[dest_key], b8)
        def fonk8(self, src_key, dest_key):
            return self.b6[src_key].fonk16(self.b6[dest_key])
        def fonk9(self):
            return len(self.b6)
        def fonk10(self):
            return iter(self.b6.values())
    class class2:
        def fonk11(self, b9):
            self.b9 = b9
            self.b10 = {}
        def fonk12(self):
            return self.b9
        def fonk13(self, dest, b8):
            self.b10[dest] = b8
        def fonk14(self):
            return self.b10.keys()
        def fonk15(self, dest):
            return self.b10[dest]
        def fonk16(self, dest):
            return dest in self.b10
    def fonk17(b14):
        b11 = {v: dict.fromkeys(b14, float('inf')) for v in b14}
        b12 = {v: dict.fromkeys(b14, None) for v in b14}
        for v in b14:
            for n in v.fonk14():
                b11[v][n] = v.fonk15(n)
                b12[v][n] = n
        for v in b14:
            b11[v][v] = 0
            b12[v][v] = None
        for a1 in b14:
            for v in b14:
                for w in b14:
                    if b11[v][w] > b11[v][a1] + b11[a1][w]:
                        b11[v][w] = b11[v][a1] + b11[a1][w]
                        b12[v][w] = b12[v][a1]
        return b11, b12
    def fonk18(b12, u, v):
        a1 = u
        b13 = []
        while b12[a1][v]:
            b13.append(a1.fonk12())
            a1 = b12[a1][v]
        b13.append(v.fonk12())
        return b13
    b14 = class1()
    for i in range(b5):
        b14.fonk4(i + 1)
    for i, j, k in b4:
        b14.fonk7(i, j, k)
    b11, b12 = fonk17(b14)
    b15 = []
    for start in b14:
        for end in b14:
            if b12[start][end]:
                b15.append([[start.fonk12(), end.fonk12()], fonk18(b12, start, end), [b11[start][end]]])
    return b15
def fonk19(b17):
    b3 = [
        (1, 2, 450),
        (1, 3, 700),
        (2, 3, 600),
        (3, 4, 800)
    ]
    b5 = 4
    return b3, b5
if b16 = = "__main__":
    b17 = 'path_to_your_file.txt'
    b15 = fonk2(b17)
    print("List for sketch:", b15)