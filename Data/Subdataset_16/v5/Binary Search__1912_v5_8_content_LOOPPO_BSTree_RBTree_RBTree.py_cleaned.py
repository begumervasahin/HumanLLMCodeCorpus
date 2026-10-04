class class1:
    def fonk1(self, b2, b1 = "Red"):
        self.b2 = b2
        self.b3 = None
        self.b4 = None
        self.b5 = None
        self.b1 = b1
    def fonk2(self):
        return self.b2
    def fonk3(self, b2):
        self.b2 = b2
    def fonk4(self, b1):
        self.b1 = b1
    def fonk5(self):
        return self.b1
    def fonk6(self):
        b6 = []
        if self.b3 is not None:
            b6.append(self.b3)
        if self.b4 is not None:
            b6.append(self.b4)
        return b6
class class2:
    def fonk7(self):
        self.b7 = class1(None, b1="Black")
        self.b8 = self.b7
    def fonk8(self, b2):
        self.b8 = class1(b2, b1="Black")
        self.b8.b5 = self.b7
        self.b8.b3 = self.b7
        self.b8.b4 = self.b7
    def fonk9(self, b10):
        b9 = b10.b4
        b10.b4 = b9.b3
        if b9.b3 != self.b7:
            b9.b3.b5 = b10
        b9.b5 = b10.b5
        if b10.b5 = = self.b7:
            self.b8 = b9
        elif b10 = = b10.b5.b3:
            b10.b5.b3 = b9
        else:
            b10.b5.b4 = b9
        b9.b3 = b10
        b10.b5 = b9
    def fonk10(self, b10):
        b9 = b10.b3
        b10.b3 = b9.b4
        if b9.b4 != self.b7:
            b9.b4.b5 = b10
        b9.b5 = b10.b5
        if b10.b5 = = self.b7:
            self.b8 = b9
        elif b10 = = b10.b5.b3:
            b10.b5.b3 = b9
        else:
            b10.b5.b4 = b9
        b9.b4 = b10
        b10.b5 = b9
    def fonk11(self, b2):
        b11 = class1(b2)
        self.fonk12(b11)
    def fonk12(self, b13):
        b9 = self.b7
        b12 = self.b8
        while b12 != self.b7:
            b9 = b12
            if b13.b2 < b12.b2:
                b12 = b12.b3
            else:
                b12 = b12.b4
        b13.b5 = b9
        if b9 = = self.b7:
            self.b8 = b13
        elif b13.b2 < b9.b2:
            b9.b3 = b13
        else:
            b9.b4 = b13
        b13.b3 = self.b7
        b13.b4 = self.b7
        b13.b1 = "Red"
        self.fonk13(b13)
    def fonk13(self, b13):
        while b13.b5.b1 = = "Red":
            if b13.b5 = = b13.b5.b5.b3:
                b9 = b13.b5.b5.b4
                if b9.b1 = = "Red":
                    b13.b5.b1 = "Black"
                    b9.b1 = "Black"
                    b13.b5.b5.b1 = "Red"
                    b13 = b13.b5.b5
                else:
                    if b13 = = b13.b5.b4:
                        b13 = b13.b5
                        self.fonk9(b13)
                    b13.b5.b1 = "Black"
                    b13.b5.b5.b1 = "Red"
                    self.fonk10(b13.b5.b5)
            else:
                b9 = b13.b5.b5.b3
                if b9.b1 = = "Red":
                    b13.b5.b1 = "Black"
                    b9.b1 = "Black"
                    b13.b5.b5.b1 = "Red"
                    b13 = b13.b5.b5
                else:
                    if b13 = = b13.b5.b3:
                        b13 = b13.b5
                        self.fonk10(b13)
                    b13.b5.b1 = "Black"
                    b13.b5.b5.b1 = "Red"
                    self.fonk9(b13.b5.b5)
        self.b8.b1 = "Black"
    def fonk14(self, b2):
        return self.fonk15(self.b8, b2)
    def fonk15(self, b14, b2):
        if b14 = = self.b7 or b2 == b14.b2:
            return b14 != self.b7
        elif b2 < b14.b2:
            return self.fonk15(b14.b3, b2)
        else:
            return self.fonk15(b14.b4, b2)
    def fonk16(self):
        def fonk17(b14):
            if b14 != self.b7:
                fonk17(b14.b3)
                print(f"{b14.b2} {b14.b1}")
                fonk17(b14.b4)
        fonk17(self.b8)