
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