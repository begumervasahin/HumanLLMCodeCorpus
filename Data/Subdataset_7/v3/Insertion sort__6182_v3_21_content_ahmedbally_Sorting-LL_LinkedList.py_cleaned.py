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
        self.b3 = b5
        if self.b4 is None:
            self.b4 = b5
        self.a1 += 1
    def fonk5(self, item):
        b5 = class1(item)
        if self.b4 is None or self.b4.b1 <= item:
            self.b4.b2 = b5
            self.b4 = b5
        else:
            b6 = self.b3
            b7 = None
            while b6 is not None and b6.b1 < item:
                b7 = b6
                b6 = b6.b2
            if b7 is None:
                b5.b2 = self.b3
                self.b3 = b5
            else:
                b5.b2 = b6
                b7.b2 = b5
        self.a1 += 1
    def fonk6(self):
        a2 = 0
        b6 = self.b3
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
        while b6 is not None and b6.b1 != item:
            b7 = b6
            b6 = b6.b2
        if b6 is not None:
            if b7 is None:
                self.b3 = b6.b2
                if self.b3 is None:
                    self.b4 = None
            else:
                b7.b2 = b6.b2
                if b7.b2 is None:
                    self.b4 = b7
            self.a1 -= 1
if b8 = = "__main__":
    b9 = class2()
    b9.fonk4(1)
    b9.fonk4(3)
    b9.fonk4(2)
    b9.fonk4(5)
    b9.fonk5(4)
    print("Length:", b9.fonk6())
    print("Does the list contain 2?", b9.fonk7(2))
    print("Does the list contain 6?", b9.fonk7(6))
    b9.fonk8(3)
    print("Length after removing:", b9.fonk6())