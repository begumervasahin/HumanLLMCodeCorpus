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
    def fonk4(self, current_node, indent_level):
        if current_node.b3 is not None:
            self.fonk4(current_node.b3, indent_level + 1)
        for _ in range(indent_level):
            print("    ", b5 = "")
        print(current_node.b1)
        print()
        if current_node.b2 is not None:
            self.fonk4(current_node.b2, indent_level + 1)
    def fonk5(self, target):
        return self.fonk6(self.b4, target)
    def fonk6(self, current_node, target):
        if current_node is None:
            return None
        if current_node.b1 = = target:
            return current_node
        elif target < current_node.b1:
            return self.fonk6(current_node.b2, target)
        else:
            return self.fonk6(current_node.b3, target)
    def fonk7(self, new_value):
        if self.b4 is None:
            self.b4 = class1.class2(new_value)
        else:
            self.fonk8(self.b4, new_value)
    def fonk8(self, current_node, new_value):
        if new_value < current_node.b1:
            if current_node.b2 is None:
                current_node.b2 = class1.class2(new_value)
            else:
                self.fonk8(current_node.b2, new_value)
        elif new_value > current_node.b1:
            if current_node.b3 is None:
                current_node.b3 = class1.class2(new_value)
            else:
                self.fonk8(current_node.b3, new_value)
    def fonk9(self):
        self.fonk10(self.b4)
    def fonk10(self, current_node):
        if current_node is None:
            return
        current_node.b2, current_node.b3 = current_node.b3, current_node.b2
        self.fonk10(current_node.b2)
        self.fonk10(current_node.b3)
def fonk11():
    b6 = class1()
    b6.b4 = class1.class2("man")
    b7 = b6.fonk5("man")
    b7.b2 = class1.class2("dog")
    b7.b3 = class1.class2("zebra")
    b6.fonk7("ape")
    b6.fonk7("elephant")
    b6.fonk7("yak")
    b6.fonk7("zorse")
    b6.fonk7("fly")
    b6.fonk3()
if b8 = = "__main__":
    fonk11()