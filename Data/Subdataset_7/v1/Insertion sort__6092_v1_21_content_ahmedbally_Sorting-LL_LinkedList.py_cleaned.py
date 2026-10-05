class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = None
        self.b4 = None
        self.a1 = 0
    def fonk3(self):
        return self.b3 is None
    def fonk4(self, item):
        b5 = class1(item)
        b5.b2 = self.b3
        if self.b3 is None:
            self.b4 = b5
        self.b3 = b5
        self.a1 += 1
    def fonk5(self, item):
        b5 = class1(item)
        b5.b2 = None
        b6 = self.b4
        b7 = None
        while b6 is not None:
            if b6.b1 > item:
                break
            else:
                b7 = b6
                b6 = b6.b2
        if b7 is None:
            b5.b2 = self.b4
            self.b4 = b5
        else:
            b5.b2 = b6
            b7.b2 = b5
    def fonk6(self):
        b6 = self.b3
        a2 = 0
        while b6 is not None:
            a2 += 1
            b6 = b6.b2
        return a2
    def fonk7(self, item):
        b6 = self.b3
        while b6 is not None:
            if b6.b1 = = item:
                return True
            b6 = b6.b2
        return False
    def fonk8(self, item):
        b6 = self.b3
        b7 = None
        b8 = False
        while not b8:
            if b6.b1 = = item:
                b8 = True
            else:
                b7 = b6
                b6 = b6.b2
        if b7 is None:
            self.b3 = b6.b2
        else:
            b7.b2 = b6.b2
        self.a1 -= 1
if b9 = = "__main__":
    b10 = class2()
    b10.fonk4(1)
    b10.fonk4(3)
    b10.fonk4(2)
    b10.fonk4(5)
    b10.fonk5(4)
    print("Length:", b10.fonk6())
    print("Is 2 in the list?", b10.fonk7(2))
    print("Is 6 in the list?", b10.fonk7(6))
    b10.fonk8(3)
    print("Length after removing:", b10.fonk6())