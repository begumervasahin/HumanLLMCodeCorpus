class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = None
    def fonk3(self, b1):
        b4 = class1(b1)
        b4.b2 = self.b3
        self.b3 = b4
    def fonk4(self, b1):
        b4 = class1(b1)
        if not self.b3:
            self.b3 = b4
            return
        b5 = self.b3
        while b5.b2:
            b5 = b5.b2
        b5.b2 = b4
    def fonk5(self):
        if not self.b3:
            return False
        if not self.b3.b2:
            self.b3 = None
            return True
        b6 = self.b3
        while b6.b2.b2:
            b6 = b6.b2
        b6.b2 = None
        return True
    def fonk6(self, b1, b7 = 0):
        if b7 = = 0:
            self.fonk3(b1)
            return
        b4 = class1(b1)
        b8 = self.b3
        for _ in range(b7 - 1):
            if b8 is None:
                raise IndexError("Index out of range")
            b8 = b8.b2
        b4.b2 = b8.b2
        b8.b2 = b4
    def fonk7(self, b7 = None):
        if not self.b3:
            return False
        if b7 is None:
            return False
        if b7 = = 0:
            self.b3 = self.b3.b2
            return True
        b8 = self.b3
        for _ in range(b7 - 1):
            if b8.b2 is None:
                raise IndexError("Index out of range")
            b8 = b8.b2
        if b8 is None or b8.b2 is None:
            raise IndexError("Index out of range")
        b8.b2 = b8.b2.b2
        return True
    def fonk8(self):
        return self.b3 is None
    def fonk9(self):
        a1 = 0
        b8 = self.b3
        while b8:
            a1 += 1
            b8 = b8.b2
        return a1
    def fonk10(self):
        b9 = "["
        b8 = self.b3
        while b8:
            b9 += str(b8.b1)
            b8 = b8.b2
            if b8:
                b9 += " -> "
        b9 += "]"
        return b9
if b10 = = "__main__":
    b11 = class2()
    print(b11.fonk8())
    b11.fonk3(1)
    b11.fonk4(2)
    b11.fonk4(3)
    print(b11)
    print(len(b11))
    b11.fonk5()
    print(b11)
    print(len(b11))
    b11.fonk6(4, 1)
    print(b11)
    print(len(b11))
    b11.fonk7(1)
    print(b11)
    print(len(b11))
    print(b11.fonk8())
