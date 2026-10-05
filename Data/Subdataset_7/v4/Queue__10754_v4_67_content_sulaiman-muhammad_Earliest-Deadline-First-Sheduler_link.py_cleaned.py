class class1:
    def fonk1(self, b1 = None, b2=None):
        self.b1 = b1
        self.b2 = b2
class class2:
    def fonk2(self):
        self.b3 = None
        self.b4 = None
    def fonk3(self, b1, position):
        b5 = class1(b1)
        b5.b2 = position.b2
        position.b2 = b5
    def fonk4(self, b1):
        b5 = class1(b1)
        if not self.b3:
            self.b3 = b5
            self.b4 = b5
        else:
            self.b4.b2 = b5
            self.b4 = b5
    def fonk5(self, b1):
        b6 = self.b3
        while b6 and b6.b1 != b1:
            b6 = b6.b2
        return b6
    def fonk6(self):
        b6 = self.b3
        while b6:
            print(b6.b1)
            b6 = b6.b2
    def fonk7(self, b1):
        if not self.b3:
            b5 = class1(b1)
            self.b3 = b5
            self.b4 = b5
        else:
            b6 = self.b3
            if b6.b1.cpu > b1.cpu:
                b5 = class1(b1)
                b5.b2 = b6
                self.b3 = b5
                return
            while b6.b2 and b6.b2.b1.cpu < b1.cpu:
                b6 = b6.b2
            b5 = class1(b1)
            if not b6.b2:
                b6.b2 = b5
                self.b4 = b5
                return
            b7 = b6.b2
            b6.b2 = b5
            b5.b2 = b7
    def fonk8(self):
        b8 = None
        b9 = None
        b6 = self.b3.b2
        while b6:
            b9 = b6.b2
            b6.b2 = b8
            b8 = b6
            b6 = b9
        self.b3.b2 = b8
        self.fonk6()
    def fonk9(self, b1):
        b5 = class1(b1)
        if not self.b3:
            self.b3 = b5
            self.b4 = b5
        else:
            b5.b2 = self.b3
            self.b3 = b5
    def fonk10(self):
        if not self.b3:
            print("List is empty")
            return
        if not self.b3.b2:
            b7 = self.b3
            self.b3 = None
            self.b4 = None
            return b7
        else:
            b7 = self.b3
            self.b3 = self.b3.b2
            b7.b2 = None
            return b7
def fonk11():
    b10 = class2()
    b10.fonk9(1)
    b10.fonk7(3)
    b10.fonk6()
    print("Tail:", b10.b4.b1)
    b10.fonk10()
    b10.fonk10()
    b10.fonk10()
    b10.fonk10()
    b10.fonk10()
if b11 = = "__main__":
    fonk11()