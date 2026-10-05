
class class1:
    class class2:
        def fonk1(self, b1):
            self.b1 = b1
            self.b2 = None
            self.b3 = None
    def fonk2(self):
        self.b4 = None
    def fonk3(self):
        class1.fonk4(self.b4, 0)
    @staticmethod
    def fonk4(b7, indent_level):
        if b7.b3:
            class1.fonk4(b7.b3, indent_level + 1)
        for _ in range(indent_level):
            print("    ", b5 = "")
        print(b7.b1)
        print()
        if b7.b2:
            class1.fonk4(b7.b2, indent_level + 1)
    def fonk5(self, target):
        return class1.fonk6(self.b4, target)
    @staticmethod
    def fonk6(tree_ptr, target):
        if tree_ptr is None:
            return None
        if tree_ptr.b1 = = target:
            return tree_ptr
        elif target < tree_ptr.b1:
            return class1.fonk6(tree_ptr.b2, target)
        else:
            return class1.fonk6(tree_ptr.b3, target)
    def fonk7(self, new_value):
        if self.b4 is None:
            self.b4 = class1.class2(new_value)
        else:
            class1.fonk8(self.b4, new_value)
    @staticmethod
    def fonk8(tree_ptr, new_value):
        if new_value < tree_ptr.b1:
            if tree_ptr.b2 is None:
                tree_ptr.b2 = class1.class2(new_value)
            else:
                class1.fonk8(tree_ptr.b2, new_value)
        elif new_value > tree_ptr.b1:
            if tree_ptr.b3 is None:
                tree_ptr.b3 = class1.class2(new_value)
            else:
                class1.fonk8(tree_ptr.b3, new_value)
    def fonk9(self):
        class1.fonk10(self.b4)
    @staticmethod
    def fonk10(b7):
        pass
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