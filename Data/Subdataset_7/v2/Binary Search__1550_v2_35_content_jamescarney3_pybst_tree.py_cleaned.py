class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
    def fonk2(self, b1):
        if b1 < self.b1:
            if not self.b2:
                self.b2 = class1(b1)
                return self.b2
            else:
                return self.b2.fonk5(b1)
        elif b1 > self.b1:
            if not self.b3:
                self.b3 = class1(b1)
                return self.b3
            else:
                return self.b3.fonk5(b1)
        return None
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
        return self.b4
    def fonk6(self, b1):
        if not self.b4:
            return None
        elif self.b4.b1 = = b1:
            return self.b4
        else:
            return self.b4.fonk6(b1)
if b5 = = "__main__":
    b6 = class2()
    b6.fonk5(5)
    b6.fonk5(3)
    b6.fonk5(7)
    b6.fonk5(2)
    b6.fonk5(4)
    b6.fonk5(6)
    b6.fonk5(8)
    print("In-order traversal:")
    def fonk7(node):
        if not node:
            return
        fonk7(node.b2)
        print(node.b1, b7 = " ")
        fonk7(node.b3)
    fonk7(b6.b4)
    print()
    print("Looking up values:")
    print("Value 3:", b6.fonk6(3).b1 if b6.fonk6(3) else "Not found")
    print("Value 6:", b6.fonk6(6).b1 if b6.fonk6(6) else "Not found")
    print("Value 9:", b6.fonk6(9).b1 if b6.fonk6(9) else "Not found")