class class1:
    def fonk1(self, val):
        self.b1 = None
        self.b2 = None
        self.b3 = None
        self.b4 = val
    def fonk2(self, child_node):
        self.b1 = child_node
        child_node.b3 = self
    def fonk3(self, child_node):
        self.b2 = child_node
        child_node.b3 = self
    def fonk4(self):
        print(self.b1)
    def fonk5(self):
        print(self.b2)
    def fonk6(self):
        print(self.b4)
    def fonk7(self):
        print(self.b3)
if b5 = = "__main__":
    b6 = class1(10)
    b7 = class1(5)
    b8 = class1(15)
    b6.fonk2(b7)
    b6.fonk3(b8)
    b6.fonk6()
    b6.fonk4()
    b6.fonk5()
    b7.fonk7()
    b8.fonk7()
