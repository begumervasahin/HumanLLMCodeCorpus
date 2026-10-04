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
        if node is not None:
            if node.b3 is not None:
                self.fonk4(node.b3, indent_level + 1)
            print("    " * indent_level + str(node.b1))
            if node.b2 is not None:
                self.fonk4(node.b2, indent_level + 1)
    def fonk5(self, target):
        return self.fonk6(self.b4, target)
    def fonk6(self, node, target):
        if node is None:
            return None
        if node.b1 = = target:
            return node
        elif target < node.b1:
            return self.fonk6(node.b2, target)
        else:
            return self.fonk6(node.b3, target)
    def fonk7(self, new_value):
        if self.b4 is None:
            self.b4 = class1.class2(new_value)
        else:
            self.fonk8(self.b4, new_value)
    def fonk8(self, node, new_value):
        if new_value < node.b1:
            if node.b2 is None:
                node.b2 = class1.class2(new_value)
            else:
                self.fonk8(node.b2, new_value)
        elif new_value > node.b1:
            if node.b3 is None:
                node.b3 = class1.class2(new_value)
            else:
                self.fonk8(node.b3, new_value)
    def fonk9(self):
        self.fonk10(self.b4)
    def fonk10(self, node):
        if node is not None:
            node.b2, node.b3 = node.b3, node.b2
            self.fonk10(node.b2)
            self.fonk10(node.b3)
def fonk11():
    b5 = class1()
    b5.b4 = class1.class2("man")
    b6 = b5.fonk5("man")
    if b6:
        b6.b2 = class1.class2("dog")
        b6.b3 = class1.class2("zebra")
    b5.fonk7("ape")
    b5.fonk7("elephant")
    b5.fonk7("yak")
    b5.fonk7("zorse")
    b5.fonk7("fly")
    print("Tree before flipping:")
    b5.fonk3()
    b5.fonk9()
    print("\nTree after flipping:")
    b5.fonk3()
if b7 = = "__main__":
    fonk11()