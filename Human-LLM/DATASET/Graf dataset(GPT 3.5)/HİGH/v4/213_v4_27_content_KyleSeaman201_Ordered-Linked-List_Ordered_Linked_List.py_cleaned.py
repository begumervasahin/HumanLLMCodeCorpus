class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
    def fonk2(self):
        return self.b1
    def fonk3(self):
        return self.b2
    def fonk4(self, new_value):
        self.b1 = new_value
    def fonk5(self, new_next):
        self.b2 = new_next
    def fonk6(self):
        return str(self.b1)
    b3 = __str__
class class2:
    def fonk7(self):
        self.b4 = None
        self.b5 = None
        self.a1 = 0
    def fonk8(self, b1):
        b6 = class1(b1)
        if self.b4 is None:
            self.b4 = b6
            self.b5 = b6
        elif self.b4.b1 > b6.b1:
            b6.b2 = self.b4
            self.b4 = b6
        elif self.b5.b1 < b6.b1:
            self.b5.b2 = b6
            self.b5 = b6
        else:
            b7 = self.b4
            while b7.b1 < b6.b1:
                b8 = b7
                b7 = b7.b2
            b8.b2 = b6
            b6.b2 = b7
    def fonk9(self, b1):
        if self.b4.b1 = = b1:
            self.b4 = self.b4.b2
        elif self.b5.b1 = = b1:
            b7 = self.b4
            while b7.b2 != self.b5:
                b7 = b7.b2
            self.b5 = b7
            self.b5.b2 = None
        else:
            b7 = self.b4
            while b7.b1 != b1:
                b8 = b7
                b7 = b7.b2
            b8.b2 = b7.b2
            b7.b2 = None
    def fonk10(self, b1):
        b7 = self.b4
        while b7 is not None:
            if b7.b1 = = b1:
                return True
            b7 = b7.b2
        return False
    def fonk11(self):
        b1 = self.b5.b1
        b7 = self.b4
        while b7.b2 != self.b5:
            b7 = b7.b2
        self.b5 = b7
        self.b5.b2 = None
        return b1
    def fonk12(self):
        return self.b4 is None
    def fonk13(self):
        a1 = 0
        b7 = self.b4
        while b7 is not None:
            a1 += 1
            b7 = b7.b2
        return a1
    def fonk14(self):
        b7 = self.b4
        while b7:
            print(b7.fonk2(), b9 = ' ')
            b7 = b7.fonk3()