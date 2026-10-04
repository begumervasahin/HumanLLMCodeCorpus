class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
    def fonk2(self, b1):
        if b1 < self.b1:
            if self.b2 is None:
                self.b2 = class1(b1)
            else:
                self.b2.fonk5(b1)
        elif b1 > self.b1:
            if self.b3 is None:
                self.b3 = class1(b1)
            else:
                self.b3.fonk5(b1)
    def fonk3(self, b1):
        if b1 = = self.b1:
            return self
        elif b1 < self.b1 and self.b2:
            return self.b2.fonk6(b1)
        elif b1 > self.b1 and self.b3:
            return self.b3.fonk6(b1)
        return None
class class2:
    def fonk4(self):
        self.b4 = None
    def fonk5(self, b1):
        if self.b4 is None:
            self.b4 = class1(b1)
        else:
            self.b4.fonk5(b1)
    def fonk6(self, b1):
        if self.b4 is None:
            return None
        return self.b4.fonk6(b1)
b5 = class2()
b5.fonk5(10)
b5.fonk5(5)
b5.fonk5(15)
b5.fonk5(3)
b5.fonk5(7)
b5.fonk5(12)
b5.fonk5(18)
b6 = b5.fonk6(7)
if b6:
    print(f"Node with b1 {b6.b1} found in the tree.")
else:
    print("Value not found in the tree.")
b6 = b5.fonk6(6)
if b6:
    print(f"Node with b1 {b6.b1} found in the tree.")
else:
    print("Value not found in the tree.")