import copy
from importer import *
class class1:
    def fonk1(self):
        self.b1 = None
        self.b2 = None
        self.a1 = 0
        self.a2 = 0
        self.a3 = 0
        self.a4 = 0
        self.a5 = 0.0
    def fonk2(self):
        x, y, b6, b3 = self.b2
        self.a1 = x
        self.a2 = y - 555
        self.a3 = b6
        self.a4 = b3
    def fonk3(self):
        return self.a5 >= MIN_CONTOUR_AREA
def fonk4(initial_value, *dimensions):
    b4 = initial_value
    for dim in reversed(dimensions):
        b4 = [copy.deepcopy(b4) for _ in range(dim)]
    return b4
class class2:
    def fonk5(self, b5, b6, b7):
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
    def fonk6(self):
        return f"class2(b5 = {self.b5}, b6={self.b6}, b7={self.b7})"