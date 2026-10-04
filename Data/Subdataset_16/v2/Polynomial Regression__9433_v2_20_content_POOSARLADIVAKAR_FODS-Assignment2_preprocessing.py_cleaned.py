import numpy as np
class class1:
    def fonk1(self, arr):
        self.b1 = np.b1(arr)
        self.b2 = np.b2(arr)
    def fonk2(self, arr):
        return (arr - self.b1) / self.b2
class class2:
    def fonk3(self, arr):
        self.b3 = np.b3(arr)
        self.b4 = np.b4(arr)
    def fonk4(self, arr):
        return (arr - self.b3) / (self.b4 - self.b3)
    def fonk5(self, arr):
        return arr * (self.b4 - self.b3) + self.b3
if b5 = = "__main__":
    b6 = np.array([1, 2, 3, 4, 5])
    b7 = class1()
    b7.fonk3(b6)
    b8 = b7.fonk4(b6)
    print("Normalized b6:", b8)
    b9 = class2()
    b9.fonk3(b6)
    b10 = b9.fonk4(b6)
    print("Min-Max scaled b6:", b10)
    b11 = b9.fonk5(b10)
    print("Inverse transformed b6:", b11)