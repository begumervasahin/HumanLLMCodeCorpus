import os
from numpy import *
'''
    Function: read MINST image data, including training and testing data(images with labels)
    Training images: 60000
    Testing images: 10000
    Image width: 28
    Image height: 28
    Header: 16 Bytes, not analyzed, just skip the header.
'''
class class1:
    def fonk1(self, train_file, b3, test_file, b4):
        self.b1 = train_file
        self.b2 = test_file
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
        b9 = open(self.b2, "rb")
        print (self.b2)
        if b9 is "":
            return
        self.fonk10(b9)
        for i in range(0, self.a2):
            self.b6[i] = fromstring(b9.read(self.a3 * self.a4), uint8)
    def fonk7(self):
        b9 = open(self.b1, "rb")
        if b9 is "":
            return
        self.fonk10(b9)
        for i in range(0, self.a1):
            self.b5[i] = fromstring(b9.read(self.a3*self.a4), uint8)
    def fonk8(self):
        b9 = open(self.b4, "rb")
        if b9 is "":
            return
        self.fonk10(b9, 8)
        self.b8 = fromstring(b9.read(self.a2), uint8)
    def fonk9(self):
        b9 = open(self.b3, "rb")
        if b9 is "":
            return
        self.fonk10(b9, 8)
        self.b7 = fromstring(b9.read(self.a1), uint8)
    def fonk10(self, b9, b10 = 16):
        b9.seek(b10, os.SEEK_CUR);