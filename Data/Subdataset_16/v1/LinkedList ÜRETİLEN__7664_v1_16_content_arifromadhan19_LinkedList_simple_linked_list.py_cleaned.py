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
            print(b4.b1, b5 = ' ')
            b4 = b4.b2
        print()
    def fonk4(self, b1):
        b6 = class1(b1)
        if self.b3 is None:
            self.b3 = b6
        else:
            b7 = self.b3
            while b7.b2:
                b7 = b7.b2
            b7.b2 = b6
    def fonk5(self, b1):
        b6 = class1(b1)
        b6.b2 = self.b3
        self.b3 = b6
    def fonk6(self, b1, b8):
        b6 = class1(b1)
        if b8 = = 0:
            b6.b2 = self.b3
            self.b3 = b6
        else:
            b7 = self.b3
            a1 = 0
            while a1 < b8 - 1 and b7:
                b7 = b7.b2
                a1 += 1
            if b7 is None:
                print("Position out of bounds")
            else:
                b6.b2 = b7.b2
                b7.b2 = b6
    def fonk7(self, b8):
        if self.b3 is None:
            print("List is empty")
            return
        b4 = self.b3
        if b8 = = 0:
            self.b3 = b4.b2
            b4 = None
            return
        for i in range(b8 - 1):
            b4 = b4.b2
            if b4 is None:
                break
        if b4 is None or b4.b2 is None:
            print("Position out of bounds")
            return
        b2 = b4.b2.b2
        b4.b2 = None
        b4.b2 = b2
    def fonk8(self):
        b9 = []
        b7 = self.b3
        while b7:
            b9.append(b7)
            b7 = b7.b2
        while b9:
            b10 = b9.pop()
            print(b10.b1, b5 = ' ')
        print()
    def fonk9(self):
        b7 = self.b3
        b11 = None
        while b7:
            b12 = b7.b2
            b7.b2 = b11
            b11 = b7
            b7 = b12
        self.b3 = b11
if b13 = = '__main__':
    b14 = class2()
    b14.fonk5(1)
    b14.fonk6(2, 1)
    b14.fonk6(3, 2)
    b14.fonk4(4)
    print("Linked list:")
    b14.fonk3()
    print("Reversed linked list:")
    b14.fonk9()
    b14.fonk3()