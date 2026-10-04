import os
import numpy as np
class class1:
    def fonk1(self, b2, b3, b4, b1 = 28, b5=28):
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b1 = b1
        self.b5 = b5
        self.b6 = np.zeros((self.b4, self.b1 * self.b5), b8=np.uint8)
        self.b7 = np.zeros(self.b4, b8=np.uint8)
    def fonk2(self):
        with open(self.b2, "rb") as file:
            self.fonk4(file)
            for i in range(self.b4):
                self.b6[i] = np.frombuffer(file.read(self.b1 * self.b5), b8 = np.uint8)
    def fonk3(self):
        with open(self.b3, "rb") as file:
            self.fonk4(file, 8)
            self.b7 = np.frombuffer(file.read(self.b4), b8=np.uint8)
    @staticmethod
    def fonk4(file, b9 = 16):
        file.seek(b9, os.SEEK_CUR)
    def fonk5(self):
        return self.b6
    def fonk6(self):
        return self.b7
class class2:
    def fonk7(self, b12, b13, b14, b15):
        self.b10 = class1(b12, b13, 60000)
        self.b11 = class1(b14, b15, 10000)
    def fonk8(self):
        self.b10.fonk2()
        self.b10.fonk3()
        self.b11.fonk2()
        self.b11.fonk3()
    def fonk9(self):
        return self.b10.fonk5(), self.b10.fonk6()
    def fonk10(self):
        return self.b11.fonk5(), self.b11.fonk6()
def fonk11():
    b12 = input("Enter the training image file path: ")
    b13 = input("Enter the training label file path: ")
    b14 = input("Enter the testing image file path: ")
    b15 = input("Enter the testing label file path: ")
    b16 = class2(b12, b13, b14, b15)
    b16.fonk8()
    train_data, b17 = b16.fonk9()
    test_data, b18 = b16.fonk10()
    print(f"Training b6 shape: {train_data.shape}")
    print(f"Training b7 shape: {b17.shape}")
    print(f"Testing b6 shape: {test_data.shape}")
    print(f"Testing b7 shape: {b18.shape}")
if b19 = = "__main__":
    fonk11()