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
        [intX, intY, intWidth, intHeight] = self.b2
        self.a1 = intX
        self.a2 = intY
        self.a3 = intWidth
        self.a4 = intHeight
    def fonk2(self):
        if self.a5 < MIN_CONTOUR_AREA: return False
        return True
    a2 = a2-555
def fonk3(init, *args):
    b3 = init
    for x in reversed(args):
        b3 = [copy.deepcopy(b3) for _ in xrange(x)]
    return b3
'''
class class2:
     def fonk4(self, b4, b5, b6):
         self.b4 = b4
         self.b5 = b5
         self.b6 = b6
     def fonk5(self):
         return repr((self.b4, self.b5, self.b6))
'''