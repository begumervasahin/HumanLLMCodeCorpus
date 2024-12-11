import os
import numpy as np
class class1:
    def fonk1(self, b1, b3, b2, b4):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.a1 = 60000
        self.a2 = 10000
        self.a3 = 28
        self.a4 = 28
        self.b5 = np.zeros((self.a1, self.a3 * self.a4), b9=np.uint8)
        self.b6 = np.zeros((self.a2, self.a3 * self.a4), b9=np.uint8)
        self.b7 = np.zeros(self.a1, b9=np.uint8)
        self.b8 = np.zeros(self.a2, b9=np.uint8)
    def fonk2(self):
        return self.b5
    def fonk3(self):
        return self.b7
    def fonk4(self):
        return self.b6
    def fonk5(self):
        return self.b8
    def fonk6(self):
        with open(self.b2, "rb") as file:
            self.fonk10(file)
            for i in range(self.a2):
                self.b6[i] = np.frombuffer(file.read(self.a3 * self.a4), b9 = np.uint8)
    def fonk7(self):
        with open(self.b1, "rb") as file:
            self.fonk10(file)
            for i in range(self.a1):
                self.b5[i] = np.frombuffer(file.read(self.a3 * self.a4), b9 = np.uint8)
    def fonk8(self):
        with open(self.b4, "rb") as file:
            self.fonk10(file, 8)
            self.b8 = np.frombuffer(file.read(self.a2), b9=np.uint8)
    def fonk9(self):
        with open(self.b3, "rb") as file:
            self.fonk10(file, 8)
            self.b7 = np.frombuffer(file.read(self.a1), b9=np.uint8)
    def fonk10(self, file, b10 = 16):
        file.seek(b10, os.SEEK_CUR)
b1 = "train-images.idx3-ubyte"
b3 = "train-labels.idx1-ubyte"
b2 = "t10k-images.idx3-ubyte"
b4 = "t10k-labels.idx1-ubyte"
b11 = class1(b1, b3, b2, b4)
b11.fonk7()
b11.fonk9()
b11.fonk6()
b11.fonk8()
b12 = b11.fonk2()
b13 = b11.fonk3()
b14 = b11.fonk4()
b15 = b11.fonk5()