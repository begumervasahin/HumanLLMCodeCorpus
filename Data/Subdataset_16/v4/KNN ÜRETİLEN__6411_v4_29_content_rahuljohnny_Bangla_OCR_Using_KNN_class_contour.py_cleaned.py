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
        intX, intY, intWidth, b3 = self.b2
        self.a1 = intX
        self.a2 = intY - 555
        self.a3 = intWidth
        self.a4 = b3
    def fonk3(self):
        return self.a5 >= MIN_CONTOUR_AREA
def fonk4(init, *args):
    b4 = init
    for x in reversed(args):
        b4 = [copy.deepcopy(b4) for _ in range(x)]
    return b4
class class2:
    def fonk5(self, b5, b6, b7):
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
    def fonk6(self):
        return f"class2(b5 = {self.b5}, b6={self.b6}, b7={self.b7})"