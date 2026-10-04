class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
        self.b4 = None
        self.b5 = "Red"
    def fonk2(self):
        return [child for child in [self.b2, self.b3] if child]
    def fonk3(self):
        return f"Node(b1 = {self.b1}, b5={self.b5})"
class class2:
    def fonk4(self):
        self.b6 = class1(None)
        self.b6.b5 = "Black"
        self.b7 = self.b6
    def fonk5(self, b1):
        self.b7 = class1(b1)
        self.b7.b5 = "Black"
        self.b7.b4 = self.b6
        self.b7.b2 = self.b6
        self.b7.b3 = self.b6
    def fonk6(self, b9):
        b8 = b9.b3
        b9.b3 = b8.b2
        if b8.b2 != self.b6:
            b8.b2.b4 = b9
        b8.b4 = b9.b4
        if b9.b4 = = self.b6:
            self.b7 = b8
        elif b9 = = b9.b4.b2:
            b9.b4.b2 = b8
        else:
            b9.b4.b3 = b8
        b8.b2 = b9
        b9.b4 = b8
    def fonk7(self, b9):
        b8 = b9.b2
        b9.b2 = b8.b3
        if b8.b3 != self.b6:
            b8.b3.b4 = b9
        b8.b4 = b9.b4
        if b9.b4 = = self.b6:
            self.b7 = b8
        elif b9 = = b9.b4.b2:
            b9.b4.b2 = b8
        else:
            b9.b4.b3 = b8
        b8.b3 = b9
        b9.b4 = b8
    def fonk8(self, b1):
        b10 = class1(b1)
        if self.b7 is self.b6:
            self.fonk5(b1)
        else:
            self.fonk9(b10)
    def fonk9(self, b12):
        b8 = self.b6
        b11 = self.b7
        while b11 != self.b6:
            b8 = b11
            if b12.b1 < b11.b1:
                b11 = b11.b2
            else:
                b11 = b11.b3
        b12.b4 = b8
        if b12.b1 < b8.b1:
            b8.b2 = b12
        else:
            b8.b3 = b12
        b12.b2 = self.b6
        b12.b3 = self.b6
        self.fonk10(b12)
    def fonk10(self, b12):
        while b12.b4.b5 = = "Red":
            if b12.b4 = = b12.b4.b4.b2:
                b8 = b12.b4.b4.b3
                if b8.b5 = = "Red":
                    self.fonk11(b12, b8)
                else:
                    if b12 = = b12.b4.b3:
                        b12 = b12.b4
                        self.fonk6(b12)
                    self.fonk12(b12)
            else:
                b8 = b12.b4.b4.b2
                if b8.b5 = = "Red":
                    self.fonk11(b12, b8)
                else:
                    if b12 = = b12.b4.b2:
                        b12 = b12.b4
                        self.fonk7(b12)
                    self.fonk13(b12)
        self.b7.b5 = "Black"
    def fonk11(self, b12, b8):
        b12.b4.b5 = "Black"
        b8.b5 = "Black"
        b12.b4.b4.b5 = "Red"
        b12 = b12.b4.b4
    def fonk12(self, b12):
        b12.b4.b5 = "Black"
        b12.b4.b4.b5 = "Red"
        self.fonk7(b12.b4.b4)
    def fonk13(self, b12):
        b12.b4.b5 = "Black"
        b12.b4.b4.b5 = "Red"
        self.fonk6(b12.b4.b4)
    def fonk14(self, b1):
        return self.fonk15(self.b7, b1)
    def fonk15(self, b11, b1):
        if b11 = = self.b6 or b1 == b11.b1:
            return b11 != self.b6
        if b1 < b11.b1:
            return self.fonk15(b11.b2, b1)
        else:
            return self.fonk15(b11.b3, b1)
    def fonk16(self):
        def fonk17(node):
            if node != self.b6:
                fonk17(node.b2)
                print(f"{node.b1} ({node.b5})")
                fonk17(node.b3)
        fonk17(self.b7)
if b13 = = "__main__":
    b14 = class2()
    b14.fonk8(10)
    b14.fonk8(20)
    b14.fonk8(30)
    b14.fonk8(15)
    print("In-order traversal of the Red-Black Tree:")
    b14.fonk16()
    print("\nFinding 15 in the tree:")
    print("Found!" if b14.fonk14(15) else "Not found!")
    print("\nFinding 25 in the tree:")
    print("Found!" if b14.fonk14(25) else "Not found!")