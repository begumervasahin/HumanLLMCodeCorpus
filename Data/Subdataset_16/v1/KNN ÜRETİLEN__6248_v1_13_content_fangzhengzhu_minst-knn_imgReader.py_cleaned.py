import os
import numpy as np
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
            if not fr:
                return
            self.fonk10(fr)
            for i in range(self.a2):
                self.b6[i] = np.frombuffer(fr.read(self.a3 * self.a4), b9 = np.uint8)
    def fonk7(self):
        with open(self.b1, "rb") as fr:
            if not fr:
                return
            self.fonk10(fr)
            for i in range(self.a1):
                self.b5[i] = np.frombuffer(fr.read(self.a3 * self.a4), b9 = np.uint8)
    def fonk8(self):
        with open(self.b4, "rb") as fr:
            if not fr:
                return
            self.fonk10(fr, 8)
            self.b8 = np.frombuffer(fr.read(self.a2), b9=np.uint8)
    def fonk9(self):
        with open(self.b3, "rb") as fr:
            if not fr:
                return
            self.fonk10(fr, 8)
            self.b7 = np.frombuffer(fr.read(self.a1), b9=np.uint8)
    def fonk10(self, fr, b10 = 16):
        fr.seek(b10, os.SEEK_CUR)
if b11 = = "__main__":
    print("Place the MNIST b12 files in the same directory as the script")
    b1 = input("Enter the name of the training image file: ")
    b3 = input("Enter the name of the training label file: ")
    b2 = input("Enter the name of the testing image file: ")
    b4 = input("Enter the name of the testing label file: ")
    b12 = class1(b1, b3, b2, b4)
    b12.fonk7()
    b12.fonk9()
    b12.fonk6()
    b12.fonk8()
    print("Training images and labels read successfully")
    print("Testing images and labels read successfully")