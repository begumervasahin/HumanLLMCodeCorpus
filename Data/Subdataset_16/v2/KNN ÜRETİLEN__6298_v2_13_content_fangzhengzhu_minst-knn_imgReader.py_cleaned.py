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
        self.fonk10(self.b2, self.b6, self.a2)
    def fonk7(self):
        self.fonk10(self.b1, self.b5, self.a1)
    def fonk8(self):
        self.fonk11(self.b4, self.b8, self.a2)
    def fonk9(self):
        self.fonk11(self.b3, self.b7, self.a1)
    def fonk10(self, file_path, data_set, num_images):
        with open(file_path, "rb") as file:
            if not file:
                print(f"Error: {file_path} not found.")
                return
            self.fonk12(file)
            for i in range(num_images):
                data_set[i] = np.frombuffer(file.read(self.a3 * self.a4), b9 = np.uint8)
    def fonk11(self, file_path, label_set, num_labels):
        with open(file_path, "rb") as file:
            if not file:
                print(f"Error: {file_path} not found.")
                return
            self.fonk12(file, 8)
            label_set[:] = np.frombuffer(file.read(num_labels), b9 = np.uint8)
    def fonk12(self, file, b10 = 16):
        file.seek(b10, os.SEEK_CUR)
if b11 = = "__main__":
    print("Place the MNIST b12 files in the same directory as this script.")
    b1 = input("Enter the name of the training image file: ")
    b3 = input("Enter the name of the training label file: ")
    b2 = input("Enter the name of the testing image file: ")
    b4 = input("Enter the name of the testing label file: ")
    b12 = class1(b1, b3, b2, b4)
    b12.fonk7()
    b12.fonk9()
    b12.fonk6()
    b12.fonk8()
    print("Training images and labels read successfully.")
    print("Testing images and labels read successfully.")