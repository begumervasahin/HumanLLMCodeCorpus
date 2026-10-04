class class1:
    def fonk1(self, b2, b1 = None):
        self.b2 = b2
        self.b3 = None
        self.b4 = None
        self.b1 = b1
        self.a1 = 0
class class2:
    def fonk2(self):
        self.b5 = None
    def fonk3(self, b2):
        if not self.b5:
            self.b5 = class1(b2)
            return self.b5
        b6 = self.b5
        b1 = None
        while b6:
            b1 = b6
            if b2 < b6.b2:
                b6 = b6.b3
            else:
                b6 = b6.b4
        b7 = class1(b2, b1)
        if b2 < b1.b2:
            b1.b3 = b7
        else:
            b1.b4 = b7
        return b7
    def fonk4(self, b2):
        b8 = self.fonk5(b2, self.b5)
        if b8 is None:
            return None
        if b8.b3 and b8.b4:
            b9 = self.fonk6(b8.b4)
            b8.b2 = b9.b2
            b8 = b9
        b10 = b8.b3 if b8.b3 else b8.b4
        if b10:
            b10.b1 = b8.b1
        if b8.b1:
            if b8 = = b8.b1.b3:
                b8.b1.b3 = b10
            else:
                b8.b1.b4 = b10
        else:
            self.b5 = b10
        return b8
    def fonk5(self, b2, b8):
        while b8 and b8.b2 != b2:
            b8 = b8.b3 if b2 < b8.b2 else b8.b4
        return b8
    def fonk6(self, b8):
        b6 = b8
        while b6.b3:
            b6 = b6.b3
        return b6
def fonk7(b8):
    return b8.a1 if b8 else -1
def fonk8(b8):
    b8.a1 = 1 + max(fonk7(b8.b3), fonk7(b8.b4))
class class3(class2):
    def fonk9(self, b8):
        b10 = b8.b4
        b10.b1 = b8.b1
        if not b8.b1:
            self.b5 = b10
        elif b8 = = b8.b1.b3:
            b8.b1.b3 = b10
        else:
            b8.b1.b4 = b10
        b8.b4 = b10.b3
        if b8.b4:
            b8.b4.b1 = b8
        b10.b3 = b8
        b8.b1 = b10
        fonk8(b8)
        fonk8(b10)
    def fonk10(self, b8):
        b10 = b8.b3
        b10.b1 = b8.b1
        if not b8.b1:
            self.b5 = b10
        elif b8 = = b8.b1.b3:
            b8.b1.b3 = b10
        else:
            b8.b1.b4 = b10
        b8.b3 = b10.b4
        if b8.b3:
            b8.b3.b1 = b8
        b10.b4 = b8
        b8.b1 = b10
        fonk8(b8)
        fonk8(b10)
    def fonk11(self, b8):
        while b8:
            fonk8(b8)
            b11 = fonk7(b8.b3) - fonk7(b8.b4)
            if b11 > 1:
                if fonk7(b8.b3.b3) >= fonk7(b8.b3.b4):
                    self.fonk10(b8)
                else:
                    self.fonk9(b8.b3)
                    self.fonk10(b8)
            elif b11 < -1:
                if fonk7(b8.b4.b4) >= fonk7(b8.b4.b3):
                    self.fonk9(b8)
                else:
                    self.fonk10(b8.b4)
                    self.fonk9(b8)
            b8 = b8.b1
    def fonk12(self, b2):
        b8 = super().fonk12(b2)
        self.fonk11(b8)
    def fonk13(self, b2):
        b8 = super().fonk13(b2)
        if b8 and b8.b1:
            self.fonk11(b8.b1)
if b12 = = "__main__":
    b13 = class3()
    b13.fonk12(10)
    b13.fonk12(20)
    b13.fonk12(30)
    b13.fonk12(40)
    b13.fonk12(50)
    b13.fonk12(25)
    print("Root after inserts:", b13.b5.b2)
    b13.fonk13(40)
    print("Root after deleting 40:", b13.b5.b2)