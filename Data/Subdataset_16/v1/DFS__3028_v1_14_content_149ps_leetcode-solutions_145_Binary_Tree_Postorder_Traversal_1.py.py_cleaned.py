class class1(object):
    def fonk1(self, x):
        self.b1 = x
        self.b2 = None
        self.b3 = None
class class2(object):
    def fonk2(self, b8):
        b4 = []
        b5 = []
        b6 = b8
        b7 = set()
        while b6 or b5:
            if b6:
                b5.append(b6)
                b6 = b6.b2
            else:
                b6 = b5.pop()
                if b6.b3 and not (b6.b3 in b7):
                    b5.append(b6)
                    b6 = b6.b3
                else:
                    b7.add(b6)
                    b4.append(b6.b1)
                    b6 = None
        return b4
b8 = class1(1)
b8.b3 = class1(2)
b8.b3.b2 = class1(3)
b9 = class2()
b4 = b9.fonk2(b8)
print(b4)
