class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
    def fonk2(self, b1):
        if self.b2 is None:
            self.b2 = class1(b1)
        else:
            b4 = class1(b1)
            b4.b2 = self.b2
            self.b2 = b4
    def fonk3(self, b1):
        if self.b3 is None:
            self.b3 = class1(b1)
        else:
            b4 = class1(b1)
            b4.b3 = self.b3
            self.b3 = b4
    def fonk4(self):
        return self.b1
    def fonk5(self, b1):
        self.b1 = b1
    def fonk6(self):
        return self.b2
    def fonk7(self):
        return self.b3
b5 = class1(3)
b5.fonk2(4)
b5.fonk2(5)
b5.fonk3(6)
b5.fonk3(7)
b6 = b5.fonk6()
print("Left child of root:", b6.fonk4())
b6.fonk5(9)
print("Updated b5:", b5.fonk4())
b6.fonk2(11)
print("Updated b5 after inserting 11 as b2 child of 9:", b5.fonk4())
b7 = b5.fonk7().fonk7()
print("Right child of b3 child of root:", b7.fonk4())