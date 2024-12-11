class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
    def fonk2(self, b1):
        if b1 < self.b1:
            if not self.b2:
                self.b2 = class1(b1)
            else:
                self.b2.fonk5(b1)
        elif b1 > self.b1:
            if not self.b3:
                self.b3 = class1(b1)
            else:
                self.b3.fonk5(b1)
    def fonk3(self, b1):
        if self.b1 = = b1:
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
        if not self.b4:
            self.b4 = class1(b1)
        else:
            self.b4.fonk5(b1)
    def fonk6(self, b1):
        if not self.b4:
            return None
        return self.b4.fonk6(b1)
if b5 = = "__main__":
    b6 = class2()
    b7 = [5, 3, 7, 2, 4, 6, 8]
    for b1 in b7:
        b6.fonk5(b1)
    print("In-order traversal:")
    def fonk7(b10):
        if not b10:
            return
        fonk7(b10.b2)
        print(b10.b1, b8 = " ")
        fonk7(b10.b3)
    fonk7(b6.b4)
    print()
    print("Looking up b7:")
    b9 = [3, 6, 9]
    for b1 in b9:
        b10 = b6.fonk6(b1)
        if b10:
            print(f"Value {b1}: {b10.b1}")
        else:
            print(f"Value {b1}: Not found")