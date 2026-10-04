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
        if b7 < 0:
            print("Position must be a non-negative integer.")
            return
        b6 = class1(b1)
        if b7 = = 0:
            b6.b2 = self.b3
            self.b3 = b6
        else:
            b4 = self.b3
            a1 = 0
            while b4 and a1 < b7 - 1:
                b4 = b4.b2
                a1 += 1
            if b4 is None:
                print("Position out of bounds")
            else:
                b6.b2 = b4.b2
                b4.b2 = b6
    def fonk7(self, b7):
        if self.b3 is None:
            print("List is empty")
            return
        if b7 < 0:
            print("Position must be a non-negative integer.")
            return
        b8 = self.b3
        if b7 = = 0:
            self.b3 = b8.b2
            b8 = None
        else:
            b4 = self.b3
            for i in range(b7 - 1):
                if b4.b2 is None:
                    print("Position out of bounds")
                    return
                b4 = b4.b2
            if b4.b2 is None:
                print("Position out of bounds")
                return
            b9 = b4.b2.b2
            b4.b2 = None
            b4.b2 = b9
    def fonk8(self):
        b10 = []
        b4 = self.b3
        while b4:
            b10.append(b4)
            b4 = b4.b2
        while b10:
            b11 = b10.pop()
            print(b11.b1, b5 = ' ')
        print()
    def fonk9(self):
        b4 = self.b3
        b12 = None
        while b4:
            b9 = b4.b2
            b4.b2 = b12
            b12 = b4
            b4 = b9
        self.b3 = b12
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