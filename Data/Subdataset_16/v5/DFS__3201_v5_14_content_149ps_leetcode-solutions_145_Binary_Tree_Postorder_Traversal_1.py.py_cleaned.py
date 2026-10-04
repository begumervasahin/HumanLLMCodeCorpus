class class1(object):
    def fonk1(self, x):
        self.b1 = x
        self.b2 = None
        self.b3 = None
class class2(object):
    def fonk2(self, b8):
        if not b8:
            return []
        b4 = []
        b5 = []
        b6 = set()
        b7 = b8
        while b7 or b5:
            while b7:
                b5.append(b7)
                b7 = b7.b2
            b7 = b5.pop()
            if b7.b3 and b7.b3 not in b6:
                b5.append(b7)
                b7 = b7.b3
            else:
                b6.add(b7)
                b4.append(b7.b1)
                b7 = None
        return b4
b8 = class1(1)
b8.b3 = class1(2)
b8.b3.b2 = class1(3)
b9 = class2()
b4 = b9.fonk2(b8)
print(b4)
