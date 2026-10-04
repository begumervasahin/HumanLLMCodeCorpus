
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
class class2:
    def fonk2(self):
        self.b4 = None
        self.b5 = None
        self.b6 = None
    def fonk3(self, node):
        if node:
            self.fonk3(node.b2)
            print(node.b1, b7 = " ")
            self.fonk3(node.b3)
    def fonk4(self, node):
        if not node:
            return
        self.fonk4(node.b2)
        if self.b6 and node.b1 < self.b6.b1:
            if not self.b4:
                self.b4 = self.b6
            self.b5 = node
        self.b6 = node
        self.fonk4(node.b3)
    def fonk5(self, root):
        self.fonk4(root)
        if self.b4 and self.b5:
            self.b4.b1, self.b5.b1 = self.b5.b1, self.b4.b1
if b8 = = "__main__":
    b9 = class1(7)
    b9.b2 = class1(4)
    b9.b2.b2 = class1(1)
    b9.b2.b3 = class1(5)
    b9.b3 = class1(11)
    b9.b1, b9.b2.b2.b1 = b9.b2.b2.b1, b9.b1
    print("Before fixing the swap:")
    b10 = class2()
    b10.fonk3(b9)
    print()
    b10.fonk5(b9)
    print("After fixing the swap:")
    b10.fonk3(b9)
    print()