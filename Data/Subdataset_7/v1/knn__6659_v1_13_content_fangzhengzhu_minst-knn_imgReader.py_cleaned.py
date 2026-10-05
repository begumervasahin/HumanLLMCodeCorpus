import os
from numpy import *
class class1:
    def fonk1(self, b10, b3, b11, b4):
        self.b1 = b10
        self.b2 = b11
        self.b3 = b3
        self.b4 = b4
        self.a1 = 60000
        self.a2 = 10000
        self.a3 = 28
        self.a4 = 28
        self.b5 = array([[0 for x in range(0, self.a3 * self.a4)] for y in range(0, self.a1)])
        self.b6 = array([[0 for x in range(0, self.a3 * self.a4)] for y in range(0, self.a2)])
        self.b7 = ['0' for x in range(0, self.a1)]
        self.b8 = ['0' for x in range(0, self.a2)]
    def fonk2(self):
        return self.b5
    def fonk3(self):
        return self.b7
    def fonk4(self):
        return self.b6
    def fonk5(self):
        return self.b8
    def fonk6(self):
        with open(self.b2, "rb") as fr:
            self.fonk10(fr)
            for i in range(0, self.a2):
                self.b6[i] = fromstring(fr.read(self.a3 * self.a4), uint8)
    def fonk7(self):
        with open(self.b1, "rb") as fr:
            self.fonk10(fr)
            for i in range(0, self.a1):
                self.b5[i] = fromstring(fr.read(self.a3 * self.a4), uint8)
    def fonk8(self):
        with open(self.b4, "rb") as fr:
            self.fonk10(fr, 8)
            self.b8 = fromstring(fr.read(self.a2), uint8)
    def fonk9(self):
        with open(self.b3, "rb") as fr:
            self.fonk10(fr, 8)
            self.b7 = fromstring(fr.read(self.a1), uint8)
    def fonk10(self, fr, b9 = 16):
        fr.seek(b9, os.SEEK_CUR)
b10 = "train-images.idx3-ubyte"
b3 = "train-labels.idx1-ubyte"
b11 = "t10k-images.idx3-ubyte"
b4 = "t10k-labels.idx1-ubyte"
b12 = class1(b10, b3, b11, b4)
b12.fonk7()
b12.fonk9()
b12.fonk6()
b12.fonk8()
b13 = b12.fonk2()
b14 = b12.fonk3()
b15 = b12.fonk4()
b16 = b12.fonk5()