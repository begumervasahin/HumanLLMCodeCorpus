class class1:
    def fonk1(self, b1 = None, b2=None, b3=None, b4=0):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
class class2:
    def fonk2(self):
        self.b5 = None
    def fonk3(self, b5):
        b6 = b5
        b5 = b5.b3
        b6.b3 = b5.b2
        b5.b2 = b6
        return b5
    def fonk4(self, b5):
        b6 = b5
        b5 = b5.b2
        b6.b2 = b5.b3
        b5.b3 = b6
        return b5
    def fonk5(self, b5):
        b7 = b5.b2
        b5.b2 = b7.b3
        b7.b3 = b5
        return b7
    def fonk6(self, b5):
        b7 = b5.b3
        b5.b3 = b7.b2
        b7.b2 = b5
        return b7
    def fonk7(self, b5):
        if (not b5.b2 or b5.b3) and (not b5.b2.b2 or b5.b2.b3) and (
                not b5.b3.b3 or b5.b3.b2):
            return b5
        if b5.b2.b4 > b5.b3.b4:
            return self.fonk7(b5.b2)
        else:
            return self.fonk7(b5.b3)
    def fonk8(self, b5):
        if b5 is None:
            return -1
        else:
            return b5.b4
    def fonk9(self, b5, b1):
        if b5 is None:
            return class1(b1)
        elif b1 < b5.b1:
            b5.b2 = self.fonk9(b5.b2, b1)
        else:
            b5.b3 = self.fonk9(b5.b3, b1)
        b5.b4 = 1 + max(self.fonk8(b5.b2), self.fonk8(b5.b3))
        return b5
    def fonk10(self, b1):
        self.b5 = self.fonk11(self.b5, b1)
    def fonk11(self, b5, b1):
        b5 = self.fonk9(b5, b1)
        b8 = self.fonk8(b5.b2)
        b9 = self.fonk8(b5.b3)
        if b8 - b9 > 1:
            b10 = self.fonk7(b5)
            if not b10.b2:
                return self.fonk5(b10)
            elif not b10.b3:
                return self.fonk4(b10)
        elif b9 - b8 > 1:
            b10 = self.fonk7(b5)
            if not b10.b2:
                return self.fonk3(b10)
            elif not b10.b3:
                return self.fonk6(b10)
        return b5
    def fonk12(self, b1):
        self.fonk10(b1)
    def fonk13(self, b1):
        pass
    def fonk14(self):
        self.fonk15(self.b5)
        print()
    def fonk15(self, b5):
        if b5:
            self.fonk15(b5.b2)
            print(b5.b1, b11 = " ")
            self.fonk15(b5.b3)
def fonk16():
    import random
    b12 = class2()
    print(type(b12))
    for i in random.sample([j for j in range(1, 100)], 5):
        b12.fonk12(i)
    print('insert: ')
    b12.fonk12(78)
    b12.fonk12(101)
    b12.fonk12(14)
    b12.fonk14()
    print('b4: ', b12.b5.b4)
if b13 = = '__main__':
    fonk16()