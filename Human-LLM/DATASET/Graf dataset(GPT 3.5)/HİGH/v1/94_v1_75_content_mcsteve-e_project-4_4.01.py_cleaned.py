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
    def fonk4(b8, indentLevel):
        if b8.b3 != None:
            class1.fonk4(b8.b3, indentLevel + 1)
        for k in range(indentLevel):
            print("    ", b5 = "")
        print(b8.b1)
        print()
        if b8.b2 != None:
            class1.fonk4(b8.b2, indentLevel + 1)
    def fonk5(self, target):
        return class1.fonk6(self.b4, target)
    def fonk6(b6, target):
        if b6 = = None:
            return None
        if b6.b1 = = target:
            return b6
        elif target < b6.b1:
            return class1.fonk6(b6.b2, target)
        else:
            return class1.fonk6(b6.b3, target)
    def fonk7(self, new_value):
        if self.b4 = = None:
            self.b4 = class1.class2(new_value)
        else:
            class1.fonk8(self.b4, new_value)
    def fonk8(b6, new_value):
        if new_value < b6.b1:
            if b6.b2 = = None:
                b6.b2 = class1.class2(new_value)
            else:
                class1.fonk8(b6.b2, new_value)
        elif new_value > b6.b1:
            if b6.b3 = = None:
                b6.b3 = class1.class2(new_value)
            else:
                class1.fonk8(b6.b3, new_value)
    def fonk9(self):
        fonk10(self.b4)
    def fonk10(some_node):
        pass
def fonk11():
    b7 = class1()
    b7.b4 = class1.class2("man")
    b8 = b7.fonk5("man")
    b8.b2 = class1.class2("dog")
    b8.b3 = class1.class2("zebra")
    b7.fonk7("ape")
    b7.fonk7("elephant")
    b7.fonk7("yak")
    b7.fonk7("zorse")
    b7.fonk7("fly")
    b7.fonk3()
if b9 = = "__main__":
    fonk11()