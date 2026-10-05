class class1:
    def fonk1(self, b1 = None, b2=None):
        self.b1 = b1
        self.b2 = b2
class class2:
    def fonk2(self):
        self.b3 = None
        self.b4 = None
    def fonk3(self, new_value, position):
        b5 = class1(new_value)
        b5.b2 = position.b2
        position.b2 = b5
    def fonk4(self, b1):
        b5 = class1(b1)
        if not self.b3:
            self.b3 = b5
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
            print(b6.b1, b7 = " ")
            b6 = b6.b2
        print()
    def fonk7(self, b1):
        b5 = class1(b1)
        if not self.b3:
            self.b3 = b5
            self.b4 = b5
            return
        b6 = self.b3
        if b6.b1 > b1:
            b5.b2 = b6
            self.b3 = b5
            return
        while b6.b2 and b6.b2.b1 < b1:
            b6 = b6.b2
        b5.b2 = b6.b2
        b6.b2 = b5
        if not b5.b2:
            self.b4 = b5
    def fonk8(self):
        b8 = None
        b6 = self.b3
        while b6:
            b2 = b6.b2
            b6.b2 = b8
            b8 = b6
            b6 = b2
        self.b3 = b8
    def fonk9(self, b1):
        b5 = class1(b1)
        b5.b2 = self.b3
        self.b3 = b5
    def fonk10(self):
        if not self.b3:
            print("List is empty")
            return None
        b9 = self.b3
        self.b3 = self.b3.b2
        if not self.b3:
            self.b4 = None
        return b9
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
if b11 = = "__main__":
    fonk11()