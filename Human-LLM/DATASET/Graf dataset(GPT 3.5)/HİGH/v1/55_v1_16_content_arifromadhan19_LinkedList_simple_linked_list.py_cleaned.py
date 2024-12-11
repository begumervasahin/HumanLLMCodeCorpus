class class1:
    def fonk1(self, b1 = None, b2=None):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = None
    def fonk3(self):
        b4 = self.b3
        while b4:
            print(b4.b1, b5 = " ")
            b4 = b4.b2
        print()
    def fonk4(self, b1):
        if self.b3 is None:
            self.b3 = class1(b1)
        else:
            b6 = self.b3
            while b6.b2:
                b6 = b6.b2
            b6.b2 = class1(b1)
    def fonk5(self, b1):
        b6 = class1(b1)
        b6.b2 = self.b3
        self.b3 = b6
    def fonk6(self, b1, b8):
        if b8 != 0:
            b6 = self.b3
            a1 = 1
            while b8 - a1 > 0:
                b6 = b6.b2
                a1 += 1
            if b6.b2 is None:
                b6.b2 = class1(b1, None)
            else:
                b7 = b6.b2
                b6.b2 = class1(b1, b7)
        else:
            self.b3 = class1(b1, self.b3)
    def fonk7(self, b8):
        b4 = self.b3
        if b8 = = 0:
            return b4.b2
        while b8 - 1 > 0:
            self.b3 = self.b3.b2
            b8 -= 1
        self.b3.b2 = self.b3.b2.b2
        return b4
    def fonk8(self):
        if self.b3:
            b9 = [self.b3]
            while b9[-1].b2:
                b10 = b9[-1]
                b9.append(b10.b2)
            while b9:
                b10 = b9.pop()
                print(b10.b1, b5 = " ")
        print()
    def fonk9(self):
        b6 = self.b3
        b11 = None
        b12 = None
        while b6 is not None:
            b12 = b6.b2
            b6.b2 = b11
            b11 = b6
            b6 = b12
        self.b3 = b11
if b13 = = '__main__':
    b14 = class2()
    b14.fonk5(1)
    b14.fonk6(2, 1)
    b14.fonk6(3, 2)
    b14.fonk4(4)
    print("Linked list:")
    b14.fonk3()
    print("\nReverse linked list:")
    b14.fonk9()
    b14.fonk3()