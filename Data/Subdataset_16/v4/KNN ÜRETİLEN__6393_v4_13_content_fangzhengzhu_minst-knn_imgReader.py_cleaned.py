import os
import numpy as np
class class1:
    def fonk1(self, b12, b3, b13, b4):
        self.b1 = b12
        self.b2 = b13
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
        with open(self.b2, "rb") as fr:
            self.fonk10(fr)
            for i in range(self.a2):
                self.b6[i] = np.frombuffer(fr.read(self.a3 * self.a4), b9 = np.uint8)
    def fonk7(self):
        with open(self.b1, "rb") as fr:
            self.fonk10(fr)
            for i in range(self.a1):
                self.b5[i] = np.frombuffer(fr.read(self.a3 * self.a4), b9 = np.uint8)
    def fonk8(self):
        with open(self.b4, "rb") as fr:
            self.fonk10(fr, 8)
            self.b8 = np.frombuffer(fr.read(self.a2), b9=np.uint8)
    def fonk9(self):
        with open(self.b3, "rb") as fr:
            self.fonk10(fr, 8)
            self.b7 = np.frombuffer(fr.read(self.a1), b9=np.uint8)
    def fonk10(self, fr, b10 = 16):
        fr.seek(b10, os.SEEK_CUR)
if b11 = = "__main__":
    b12 = input("Enter the training image file path: ")
    b3 = input("Enter the training label file path: ")
    b13 = input("Enter the testing image file path: ")
    b4 = input("Enter the testing label file path: ")
    b14 = class1(b12, b3, b13, b4)
    b14.fonk7()
    b14.fonk9()
    b14.fonk6()
    b14.fonk8()
    b15 = b14.fonk2()
    b16 = b14.fonk3()
    b17 = b14.fonk4()
    b18 = b14.fonk5()
    print(f"Training data shape: {b15.shape}")
    print(f"Training labels shape: {b16.shape}")
    print(f"Testing data shape: {b17.shape}")
    print(f"Testing labels shape: {b18.shape}")