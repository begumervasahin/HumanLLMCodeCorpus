
class class1:
    class class2:
        def fonk1(self, b1):
            self.b1 = b1
            self.b2 = None
            self.b3 = None
    def fonk2(self):
        self.b4 = None
    def fonk3(self):
        self.fonk4(self.b4, 0)
    def fonk4(self, node, indent_level):
        if node is None:
            return
        if node.b3:
            self.fonk4(node.b3, indent_level + 1)
        print("    " * indent_level + str(node.b1))
        if node.b2:
            self.fonk4(node.b2, indent_level + 1)
    def fonk5(self, b5):
        return self.fonk6(self.b4, b5)
    def fonk6(self, node, b5):
        if node is None:
            return None
        if b5 = = node.b1:
            return node
        elif b5 < node.b1:
            return self.fonk6(node.b2, b5)
        else:
            return self.fonk6(node.b3, b5)
    def fonk7(self, b1):
        if self.b4 is None:
            self.b4 = self.class2(b1)
        else:
            self.fonk8(self.b4, b1)
    def fonk8(self, node, b1):
        if b1 < node.b1:
            if node.b2 is None:
                node.b2 = self.class2(b1)
            else:
                self.fonk8(node.b2, b1)
        elif b1 > node.b1:
            if node.b3 is None:
                node.b3 = self.class2(b1)
            else:
                self.fonk8(node.b3, b1)
    def fonk9(self):
        self.fonk10(self.b4)
    def fonk10(self, node):
        if node:
            node.b2, node.b3 = node.b3, node.b2
            self.fonk10(node.b2)
            self.fonk10(node.b3)
def fonk11():
    b6 = class1()
    b6.b4 = class1.class2("man")
    b6.fonk7("dog")
    b6.fonk7("zebra")
    b6.fonk7("ape")
    b6.fonk7("elephant")
    b6.fonk7("yak")
    b6.fonk7("zorse")
    b6.fonk7("fly")
    b6.fonk3()
if b7 = = "__main__":
    fonk11()