class class1:
    def fonk1(self, initdata):
        self.b1 = initdata
        self.b2 = None
    def fonk2(self):
        return self.b1
    def fonk3(self):
        return self.b2
    def fonk4(self, newdata):
        self.b1 = newdata
    def fonk5(self, newnext):
        self.b2 = newnext
from class1 import class1
class class2:
    def fonk6(self):
        self.b3 = None
    def fonk7(self):
        return self.b3 = = None
    def fonk8(self, b10):
        b4 = class1(b10)
        b4.fonk5(self.b3)
        self.b3 = b4
    def fonk9(self):
        b5 = self.b3
        a1 = 0
        while b5 != None:
            a1 += 1
            b5 = b5.fonk3()
        return a1
    def fonk10(self, b10):
        b5 = self.b3
        while b5 != None:
            if b5.fonk2() == b10:
                return True
            else:
                b5 = b5.fonk3()
        return False
    def fonk11(self, b10):
        b5 = self.b3
        b6 = None
        b7 = False
        while not b7:
            if b5.fonk2() == b10:
                b7 = True
                if b6 = = None:
                    self.b3 = b5.fonk3()
                else:
                    b6.fonk5(b5.fonk3())
            else:
                b6 = b5
                b5 = b5.fonk3()
    def fonk12(self):
        b5 = self.b3
        while b5.fonk3() != None:
            b8 = b5
            b9 = b5.fonk2()
            b10 = b5.fonk3()
            while b10 != None:
                if b9 > b10.fonk2():
                    b9 = b10.fonk2()
                    b8 = b10
                b10 = b10.fonk3()
            b8.fonk4(b5.fonk2())
            b5.fonk4(b9)
