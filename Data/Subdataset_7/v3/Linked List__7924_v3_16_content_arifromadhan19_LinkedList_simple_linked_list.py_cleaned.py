class class1:
    def fonk1(self, b1 = None, b11=None):
        self.b1 = b1
        self.b2 = b11
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
        b7 = class1(b1)
        b7.b2 = self.b3
        self.b3 = b7
    def fonk6(self, b1, b8):
        if b8 = = 0:
            self.fonk5(b1)
            return
        b6 = self.b3
        for _ in range(b8 - 1):
            if b6 is None:
                return
            b6 = b6.b2
        if b6 is None:
            return
        b7 = class1(b1)
        b7.b2 = b6.b2
        b6.b2 = b7
    def fonk7(self, b8):
        if b8 = = 0:
            if self.b3 is None:
                return
            b4 = self.b3
            self.b3 = self.b3.b2
            b4.b2 = None
            return b4
        b6 = self.b3
        for _ in range(b8 - 1):
            if b6 is None:
                return
            b6 = b6.b2
        if b6 is None or b6.b2 is None:
            return
        b4 = b6.b2
        b6.b2 = b6.b2.b2
        b4.b2 = None
        return b4
    def fonk8(self):
        b9 = []
        b6 = self.b3
        while b6:
            b9.append(b6.b1)
            b6 = b6.b2
        while b9:
            print(b9.pop(), b5 = " ")
        print()
    def fonk9(self):
        b10 = None
        b6 = self.b3
        while b6:
            b11 = b6.b2
            b6.b2 = b10
            b10 = b6
            b6 = b11
        self.b3 = b10
if b12 = = '__main__':
    b13 = class2()
    b13.fonk5(1)
    b13.fonk6(2, 1)
    b13.fonk6(3, 2)
    b13.fonk4(4)
    print("Linked list:")
    b13.fonk3()
    print("\nReverse linked list:")
    b13.fonk9()
    b13.fonk3()