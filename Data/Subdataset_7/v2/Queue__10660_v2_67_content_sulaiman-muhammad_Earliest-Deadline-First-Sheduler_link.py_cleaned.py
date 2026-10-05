class class1:
    def fonk1(self, b1 = None, b2=None):
        self.b1 = b1
        self.b2 = b2
class class2:
    def fonk2(self):
        self.b3 = None
        self.b4 = None
    def fonk3(self, x, pos):
        b5 = class1(x)
        b5.b2 = pos.b2
        pos.b2 = b5
    def fonk4(self, x):
        if self.b3 is None:
            b5 = class1(x)
            self.b3 = b5
            self.b4 = b5
        else:
            b5 = class1(x)
            self.b4.b2 = b5
            self.b4 = b5
    def fonk5(self, x):
        b6 = self.b3
        while b6 is not None and b6.b1 != x:
            b6 = b6.b2
        return b6
    def fonk6(self):
        b6 = self.b3
        while b6:
            print(b6.b1, b7 = " ")
            b6 = b6.b2
        print()
    def fonk7(self, x):
        if self.b3 is None:
            b5 = class1(x)
            self.b3 = b5
            self.b4 = b5
        else:
            b6 = self.b3
            if b6.b1 > x:
                b8 = class1(x)
                b8.b2 = b6
                self.b3 = b8
                return
            while b6.b2 and b6.b2.b1 < x:
                b6 = b6.b2
            b8 = class1(x)
            b8.b2 = b6.b2
            b6.b2 = b8
            if b8.b2 is None:
                self.b4 = b8
    def fonk8(self):
        b9 = None
        b6 = self.b3
        while b6:
            b2 = b6.b2
            b6.b2 = b9
            b9 = b6
            b6 = b2
        self.b3 = b9
    def fonk9(self, x):
        b5 = class1(x)
        b5.b2 = self.b3
        self.b3 = b5
    def fonk10(self):
        if self.b3 is None:
            print("List is empty")
            return
        b5 = self.b3
        self.b3 = self.b3.b2
        if self.b3 is None:
            self.b4 = None
        return b5
def fonk11():
    b10 = class2()
    b10.fonk9(1)
    b10.fonk7(3)
    b10.fonk6()
    if b10.b4:
        print("Tail:", b10.b4.b1)
    else:
        print("Tail: None")
    b10.fonk10()
    b10.fonk10()
    b10.fonk10()
    b10.fonk10()
    b10.fonk10()
if b11 = = "__main__":
    fonk11()