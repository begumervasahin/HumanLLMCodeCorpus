from importer import *
import copy
class class1():
    b1 = None
    b2 = None
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    a5 = 0.0
    def fonk1(self):
        intX, intY, intWidth, b3 = self.b2
        self.a1 = intX
        self.a2 = intY
        self.a3 = intWidth
        self.a4 = b3
    def fonk2(self):
        if self.a5 < MIN_CONTOUR_AREA:
            return False
        return True
    a2 = a2 - 555
def fonk3(init, *args):
    b4 = init
    for x in reversed(args):
        b4 = [copy.deepcopy(b4) for _ in range(x)]
    return b4
