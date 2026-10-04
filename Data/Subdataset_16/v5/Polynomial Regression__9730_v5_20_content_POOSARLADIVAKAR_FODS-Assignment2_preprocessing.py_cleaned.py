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
def fonk6():
    b5 = np.array([1, 2, 3, 4, 5])
    b6 = class1()
    b6.fonk3(b5)
    b7 = b6.fonk4(b5)
    print("Normalized b5:", b7)
    b8 = class2()
    b8.fonk3(b5)
    b9 = b8.fonk4(b5)
    print("Min-Max scaled b5:", b9)
    b10 = b8.fonk5(b9)
    print("Inverse transformed b5:", b10)
if b11 = = "__main__":
    fonk6()