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
        if current_node is not None:
            self.fonk4(current_node.b3, indent_level + 1)
            print("    " * indent_level + str(current_node.b1))
            self.fonk4(current_node.b2, indent_level + 1)
    def fonk5(self, target):
        return self.fonk6(self.b4, target)
    def fonk6(self, current_node, target):
        if current_node is None or current_node.b1 = = target:
            return current_node
        elif target < current_node.b1:
            return self.fonk6(current_node.b2, target)
        else:
            return self.fonk6(current_node.b3, target)
    def fonk7(self, new_value):
        self.b4 = self.fonk8(self.b4, new_value)
    def fonk8(self, current_node, new_value):
        if current_node is None:
            return self.class2(new_value)
        if new_value < current_node.b1:
            current_node.b2 = self.fonk8(current_node.b2, new_value)
        elif new_value > current_node.b1:
            current_node.b3 = self.fonk8(current_node.b3, new_value)
        return current_node
    def fonk9(self):
        self.fonk10(self.b4)
    def fonk10(self, current_node):
        if current_node is not None:
            current_node.b2, current_node.b3 = current_node.b3, current_node.b2
            self.fonk10(current_node.b2)
            self.fonk10(current_node.b3)
def fonk11():
    b5 = class1()
    b5.fonk7("man")
    b5.fonk7("dog")
    b5.fonk7("zebra")
    b5.fonk7("ape")
    b5.fonk7("elephant")
    b5.fonk7("yak")
    b5.fonk7("zorse")
    b5.fonk7("fly")
    b5.fonk3()
if b6 = = "__main__":
    fonk11()