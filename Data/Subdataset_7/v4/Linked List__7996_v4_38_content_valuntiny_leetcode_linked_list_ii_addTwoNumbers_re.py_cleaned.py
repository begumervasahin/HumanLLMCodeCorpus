class class1:
    def fonk1(self, x):
        self.b1 = x
        self.b2 = None
class class2:
    def fonk2(self, b5, b6):
        a1 = 0
        b3 = class1(0)
        b4 = b3
        while b5 or b6 or a1:
            if b5:
                a1 += b5.b1
                b5 = b5.b2
            if b6:
                a1 += b6.b1
                b6 = b6.b2
            b4.b2 = class1(a1 % 10)
            b4 = b4.b2
            a1
        return b3.b2
