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
        if node:
            if node.b3:
                self.fonk4(node.b3, indent_level + 1)
            print("    " * indent_level + str(node.b1))
            if node.b2:
                self.fonk4(node.b2, indent_level + 1)
    def fonk5(self, b5):
        return self.fonk6(self.b4, b5)
    def fonk6(self, node, b5):
        if not node:
            return None
        if b5 = = node.b1:
            return node
        elif b5 < node.b1:
            return self.fonk6(node.b2, b5)
        else:
            return self.fonk6(node.b3, b5)
    def fonk7(self, new_value):
        if not self.b4:
            self.b4 = class1.class2(new_value)
        else:
            self.fonk8(self.b4, new_value)
    def fonk8(self, node, new_value):
        if new_value < node.b1:
            if not node.b2:
                node.b2 = class1.class2(new_value)
            else:
                self.fonk8(node.b2, new_value)
        elif new_value > node.b1:
            if not node.b3:
                node.b3 = class1.class2(new_value)
            else:
                self.fonk8(node.b3, new_value)
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
    b7 = b6.fonk5("man")
    if b7:
        b7.b2 = class1.class2("dog")
        b7.b3 = class1.class2("zebra")
    b6.fonk7("ape")
    b6.fonk7("elephant")
    b6.fonk7("yak")
    b6.fonk7("zorse")
    b6.fonk7("fly")
    print("Tree before flipping:")
    b6.fonk3()
    b6.fonk9()
    print("\nTree after flipping:")
    b6.fonk3()
if b8 = = "__main__":
    fonk11()