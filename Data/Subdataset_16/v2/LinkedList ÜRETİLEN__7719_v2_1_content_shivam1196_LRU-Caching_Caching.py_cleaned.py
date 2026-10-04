class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.b3 = None
        self.b4 = None
class class2:
    def fonk2(self):
        self.b5 = None
        self.b6 = None
    def fonk3(self, b1, b2):
        b7 = class1(b1, b2)
        if self.b5 is None:
            self.b5 = self.b6 = b7
        else:
            self.b6.b4 = b7
            b7.b3 = self.b6
            self.b6 = b7
        return b7
    def fonk4(self, b8):
        if b8 = = self.b6:
            return
        if b8 = = self.b5:
            self.b5 = b8.b4
            if self.b5:
                self.b5.b3 = None
        else:
            b8.b3.b4 = b8.b4
            b8.b4.b3 = b8.b3
        b8.b4 = None
        b8.b3 = self.b6
        if self.b6:
            self.b6.b4 = b8
        self.b6 = b8
    def fonk5(self):
        return self.b5
    def fonk6(self, b1, b2):
        b9 = self.b5
        self.b5 = self.b5.b4
        if self.b5:
            self.b5.b3 = None
        else:
            self.b6 = None
        b7 = class1(b1, b2)
        if self.b6 is None:
            self.b5 = self.b6 = b7
        else:
            self.b6.b4 = b7
            b7.b3 = self.b6
            self.b6 = b7
        return b7
    def fonk7(self):
        b10 = self.b5
        while b10:
            print(f"Key: {b10.b1}, Value: {b10.b2}")
            b10 = b10.b4
class class3:
    def fonk8(self, capacity):
        self.b11 = {}
        self.b12 = capacity
        self.a1 = 0
        self.b13 = class2()
    def fonk9(self, b1):
        if b1 in self.b11:
            self.b13.fonk4(self.b11[b1])
            return self.b11[b1].b2
        else:
            return -1
    def fonk10(self, b1, b2):
        if self.a1 < self.b12:
            self.b11[b1] = self.b13.fonk3(b1, b2)
            self.a1 += 1
        else:
            b8 = self.b13.fonk5()
            del self.b11[b8.b1]
            self.b11[b1] = self.b13.fonk6(b1, b2)
    def fonk11(self):
        self.b13.fonk7()
if b14 = = "__main__":
    b15 = class3(5)
    b15.fonk10(1, 1)
    b15.fonk10(2, 2)
    b15.fonk10(3, 3)
    b15.fonk10(4, 4)
    b15.fonk10(5, 5)
    b15.fonk9(1)
    b15.fonk10(6, 6)
    b15.fonk10(7, 7)
    b15.fonk9(11)
    b15.fonk11()