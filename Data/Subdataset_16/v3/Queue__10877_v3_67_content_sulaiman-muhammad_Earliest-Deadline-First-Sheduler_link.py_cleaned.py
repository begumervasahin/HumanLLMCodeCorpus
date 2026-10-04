class class1:
    def fonk1(self, b1 = None, b2=None):
        self.b1 = b1
        self.b2 = b2
class class2:
    def fonk2(self):
        self.b3 = None
        self.b4 = None
    def fonk3(self, x, b6):
        b5 = class1(x)
        b5.b2 = b6.b2
        b6.b2 = b5
        if b6 = = self.b4:
            self.b4 = b5
    def fonk4(self, x):
        b5 = class1(x)
        if not self.b3:
            self.b3 = b5
            self.b4 = b5
        else:
            self.b4.b2 = b5
            self.b4 = b5
    def fonk5(self, x):
        b7 = self.b3
        while b7:
            if b7.b1 = = x:
                return b7
            b7 = b7.b2
        return False
    def fonk6(self):
        b7 = self.b3
        while b7:
            print(b7.b1)
            b7 = b7.b2
    def fonk7(self, x):
        b5 = class1(x)
        if not self.b3 or self.b3.b1 > x:
            b5.b2 = self.b3
            self.b3 = b5
            if not self.b4:
                self.b4 = b5
            return
        b7 = self.b3
        while b7.b2 and b7.b2.b1 < x:
            b7 = b7.b2
        b5.b2 = b7.b2
        b7.b2 = b5
        if not b5.b2:
            self.b4 = b5
    def fonk8(self):
        b8 = None
        b7 = self.b3
        self.b4 = self.b3
        while b7:
            b2 = b7.b2
            b7.b2 = b8
            b8 = b7
            b7 = b2
        self.b3 = b8
    def fonk9(self, x):
        b5 = class1(x)
        if not self.b3:
            self.b3 = b5
            self.b4 = b5
        else:
            b5.b2 = self.b3
            self.b3 = b5
    def fonk10(self):
        if not self.b3:
            print("empty")
            return None
        b9 = self.b3
        self.b3 = self.b3.b2
        if not self.b3:
            self.b4 = None
        b9.b2 = None
        return b9
def fonk11():
    b10 = class2()
    b10.fonk9(1)
    b10.fonk7(3)
    b10.fonk6()
    print("Tail:", b10.b4.b1 if b10.b4 else None)
    for _ in range(5):
        b10.fonk10()
if b11 = = "__main__":
    fonk11()