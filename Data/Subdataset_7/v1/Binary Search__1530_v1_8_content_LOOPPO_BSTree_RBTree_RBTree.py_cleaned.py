class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
        self.b4 = None
        self.b5 = "Red"
    def fonk2(self):
        return self.b1
    def fonk3(self, b1):
        self.b1 = b1
    def fonk4(self, b5):
        self.b5 = b5
    def fonk5(self):
        b6 = []
        if self.b2 is not None:
            b6.append(self.b2)
        if self.b3 is not None:
            b6.append(self.b3)
        return b6
    def fonk6(self):
        return self.b5
class class2:
    def fonk7(self):
        self.b7 = class1(None)
        self.b7.fonk4("Black")
        self.b8 = self.b7
    def fonk8(self, b1):
        self.b8 = class1(b1)
        self.b8.fonk4("Black")
        self.b8.b4 = self.b7
        self.b8.b2 = self.b7
        self.b8.b3 = self.b7
    def fonk9(self, b10):
        b9 = b10.b3
        b10.b3 = b9.b2
        if b9.b2 != self.b7:
            b9.b2.b4 = b10
        b9.b4 = b10.b4
        if b10.b4 = = self.b7:
            self.b8 = b9
        elif b10 = = b10.b4.b2:
            b10.b4.b2 = b9
        else:
            b10.b4.b3 = b9
        b9.b2 = b10
        b10.b4 = b9
    def fonk10(self, b10):
        b9 = b10.b2
        b10.b2 = b9.b3
        if b9.b3 != self.b7:
            b9.b3.b4 = b10
        b9.b4 = b10.b4
        if b10.b4 = = self.b7:
            self.b8 = b9
        elif b10 = = b10.b4.b2:
            b10.b4.b2 = b9
        else:
            b10.b4.b3 = b9
        b9.b3 = b10
        b10.b4 = b9
    def fonk11(self, b1):
        if self.b8 is self.b7:
            self.fonk8(b1)
        else:
            self.fonk12(class1(b1))
    def fonk12(self, b12):
        b9 = self.b7
        b11 = self.b8
        while b11 != self.b7:
            b9 = b11
            if b12.b1 < b11.b1:
                b11 = b11.b2
            else:
                b11 = b11.b3
        b12.b4 = b9
        if b12.b1 < b9.b1:
            b9.b2 = b12
        else:
            b9.b3 = b12
        b12.b2 = self.b7
        b12.b3 = self.b7
        return self.fonk13(b12)
    def fonk13(self, b12):
        while b12.b4.b5 = = "Red":
            if b12.b4 = = b12.b4.b4.b2:
                b9 = b12.b4.b4.b3
                if b9.b5 = = "Red":
                    b12.b4.b5 = "Black"
                    b9.b5 = "Black"
                    b12.b4.b4.b5 = "Red"
                    b12 = b12.b4.b4
                else:
                    if b12 = = b12.b4.b3:
                        b12 = b12.b4
                        self.fonk9(b12)
                    b12.b4.b5 = "Black"
                    b12.b4.b4.b5 = "Red"
                    self.fonk10(b12.b4.b4)
            else:
                b9 = b12.b4.b4.b2
                if b9.b5 = = "Red":
                    b12.b4.b5 = "Black"
                    b9.b5 = "Black"
                    b12.b4.b4.b5 = "Red"
                    b12 = b12.b4.b4
                else:
                    if b12 = = b12.b4.b2:
                        b12 = b12.b4
                        self.fonk10(b12)
                    b12.b4.b5 = "Black"
                    b12.b4.b4.b5 = "Red"
                    self.fonk9(b12.b4.b4)
        self.b8.b5 = "Black"
    def fonk14(self, b1):
        return self.fonk15(self.b8, b1)
    def fonk15(self, b11, b1):
        if b11 is self.b7:
            return False
        elif b1 = = b11.b1:
            return True
        elif b1 < b11.b1:
            return self.fonk15(b11.b2, b1)
        else:
            return self.fonk15(b11.b3, b1)
    def fonk16(self):
        def fonk17(v):
            if v is self.b7:
                return
            if v.b2 is not self.b7:
                fonk17(v.b2)
            print(str(v.b1) + " " + v.b5)
            if v.b3 is not self.b7:
                fonk17(v.b3)
        fonk17(self.b8)
if b13 = = "__main__":
    b14 = class2()
    b14.fonk11(10)
    b14.fonk11(20)
    b14.fonk11(30)
    b14.fonk11(15)
    b14.fonk16()