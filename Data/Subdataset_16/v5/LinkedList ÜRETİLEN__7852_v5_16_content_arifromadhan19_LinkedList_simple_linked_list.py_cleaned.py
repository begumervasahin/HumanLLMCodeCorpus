class class1:
    def fonk1(self, b1 = None):
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
        b6 = class1(b1)
        if not self.b3:
            self.b3 = b6
        else:
            b4 = self.b3
            while b4.b2:
                b4 = b4.b2
            b4.b2 = b6
    def fonk5(self, b1):
        b6 = class1(b1)
        b6.b2 = self.b3
        self.b3 = b6
    def fonk6(self, b1, b7):
        if b7 = = 0:
            self.fonk5(b1)
        else:
            b6 = class1(b1)
            b4 = self.b3
            a1 = 1
            while b4 and a1 < b7:
                b4 = b4.b2
                a1 += 1
            if b4:
                b6.b2 = b4.b2
                b4.b2 = b6
            else:
                print("Position out of bounds")
    def fonk7(self, b7):
        if not self.b3:
            return
        if b7 = = 0:
            self.b3 = self.b3.b2
        else:
            b4 = self.b3
            for _ in range(b7 - 1):
                if not b4.b2:
                    print("Position out of bounds")
                    return
                b4 = b4.b2
            if b4.b2:
                b4.b2 = b4.b2.b2
    def fonk8(self):
        b8 = []
        b4 = self.b3
        while b4:
            b8.append(b4)
            b4 = b4.b2
        while b8:
            b9 = b8.pop()
            print(b9.b1, b5 = " ")
        print()
    def fonk9(self):
        b10 = None
        b4 = self.b3
        while b4:
            b11 = b4.b2
            b4.b2 = b10
            b10 = b4
            b4 = b11
        self.b3 = b10
if b12 = = '__main__':
    b13 = class2()
    b13.fonk5(1)
    b13.fonk6(2, 1)
    b13.fonk6(3, 2)
    b13.fonk4(4)
    print("Linked list:")
    b13.fonk3()
    print("Reversed linked list:")
    b13.fonk9()
    b13.fonk3()