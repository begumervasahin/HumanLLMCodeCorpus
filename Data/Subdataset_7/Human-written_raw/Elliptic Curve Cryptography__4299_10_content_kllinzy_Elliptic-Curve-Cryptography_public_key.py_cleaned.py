from b1 import *
from point import *
class class1(object):
    b1 = None
    a1 = 0
    b2 = None
    b3 = None
    def fonk1(self, a1, k):
        self.a1 = a1
        self.b1 = Curve.make_curve(self.a1)
        self.b2 = self.b1.random_point()
        self.b3 = self.b1.multiply(k,self.b2)
    def fonk2(self):
        b4 = []
        b4.append(str(self.b1))
        b4.append(str(self.b2))
        b4.append(str(self.b3))
        return "".join(b4)
    def fonk3(a1,k):
        b5 = class1(a1,k)
        return b5