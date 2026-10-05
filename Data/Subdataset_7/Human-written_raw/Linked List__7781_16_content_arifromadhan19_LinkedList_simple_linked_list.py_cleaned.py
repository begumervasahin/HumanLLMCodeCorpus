class class1:
    def fonk1(self, b1 = None, b2=None):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = None
    def fonk3(self):
        b4 = self.b3
        while (b4):
            print (b4.b1),
            b4 = b4.b2
    def fonk4(self, b1):
        if (self.b3 = = None):
            b3 = class1(b1)
        else:
            b5 = self.b3
            while (b5.b2 != None):
                b5 = b5.b2
            b5.b2 = class1(b1)
        return self.b3
    def fonk5(self,b1):
        b5 = class1(b1)
        b5.b2 = self.b3
        self.b3 = b5
    def fonk6(self,b1,b6):
        if not b6 = = 0:
            b5 = self.b3
            a1 = 1
            while (b6 - a1 > 0):
                b5 = b5.b2
                a1 += 1
            if b5.b2 is None:
                b5.b2 = class1(b1, None)
                return self.b3
            else:
                b7 = b5.b2
                b5.b2 = class1(b1, b7)
                return self.b3
        else:
            return class1(b1, self.b3)
    def fonk7(self, b6):
        b4 = self.b3
        if b6 = = 0:
            return b4.b2
        while b6 - 1 > 0:
            b3 = self.b3.b2
            b6 -= 1
        self.b3.b2 = self.b3.b2.b2
        return b4
    def fonk8(self):
        if self.b3:
            b8 = [self.b3]
            while b8[-1].b2:
                b9 = b8[-1]
                b8.append(b9.b2)
            while b8:
                b9 = b8.pop()
                print(b9.b1)
    def fonk9(self):
        b5 = self.b3
        b10 = None
        b2 = None
        while b5 is not None:
            b2 = b5.b2
            b5.b2 = b10
            b10 = b5
            b5 = b2
        return b10
if b11 = = '__main__':
    b12 = class2()
    b12.fonk5(1)
    b12.fonk6(2,1)
    b12.fonk6(3, 2)
    b12.fonk4(4)
    print("\nlinked list")
    print("\nReverse linked list")
    b12.fonk9()
    b12.fonk3()