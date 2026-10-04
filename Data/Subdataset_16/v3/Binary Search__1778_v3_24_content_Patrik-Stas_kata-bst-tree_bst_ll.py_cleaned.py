class class1:
    def fonk1(self, b2, b3, b1 = None):
        self.b2 = b2
        self.b3 = b3
        self.b4 = None
        self.b5 = None
        self.b1 = b1
    def fonk2(self, b6):
        if b6 = = self.b4:
            self.b4 = None
        elif b6 = = self.b5:
            self.b5 = None
    def fonk3(self):
        b7 = f"b4: {self.b4.b3}" if self.b4 else "b4: None"
        b8 = f"b5: {self.b5.b3}" if self.b5 else "b5: None"
        b9 = "ROOT" if self.b1 is None else f"b1: {self.b1.b3}"
        print(f"class1({self.b3})  {b7}  {b8}  {b9}")
    def fonk4(self):
        return not self.b4 and not self.b5
    def fonk5(self):
        return self.b1 is None
    def fonk6(self, child_node):
        self.b5 = child_node
        if child_node:
            child_node.b1 = self
    def fonk7(self, child_node):
        self.b4 = child_node
        if child_node:
            child_node.b1 = self
    def fonk8(self, b10, new_child):
        if b10 = = self.b4:
            self.fonk7(new_child)
        elif b10 = = self.b5:
            self.fonk6(new_child)
        else:
            raise ValueError("The specified old child b15 was not found.")
class class2:
    def fonk9(self, b11):
        self.b11 = b11
    def fonk10(self, b12 = False):
        self.fonk11(self.b11.b14, b12)
    def fonk11(self, b15, b12):
        if b15:
            if b12:
                b15.fonk3()
            else:
                print(f"{b15.b3} ", b13 = "")
            self.fonk11(b15.b4, b12)
            self.fonk11(b15.b5, b12)
class class3:
    def fonk12(self):
        self.b14 = None
    def fonk13(self):
        return self.fonk14(self.b14)
    def fonk14(self, b15):
        if b15 is None:
            return 0
        return 1 + self.fonk14(b15.b4) + self.fonk14(b15.b5)
    def fonk15(self, b2, b3):
        if b2 is None or b3 is None:
            raise ValueError("Key and b3 cannot be None.")
        if self.b14 is None:
            self.b14 = class1(b2, b3)
        else:
            self.fonk16(self.b14, b2, b3)
    def fonk16(self, b15, b2, b3):
        if b2 = = b15.b2:
            raise ValueError(f"Duplicate b2 {b2} is not allowed.")
        elif b2 < b15.b2:
            if b15.b4 is None:
                b15.fonk7(class1(b2, b3))
            else:
                self.fonk16(b15.b4, b2, b3)
        else:
            if b15.b5 is None:
                b15.fonk6(class1(b2, b3))
            else:
                self.fonk16(b15.b5, b2, b3)
    def fonk17(self, b2):
        b15 = self.fonk18(self.b14, b2)
        return b15.b3 if b15 else None
    def fonk18(self, b15, b2):
        if b15 is None or b15.b2 = = b2:
            return b15
        if b2 < b15.b2:
            return self.fonk18(b15.b4, b2)
        return self.fonk18(b15.b5, b2)
    def fonk19(self, b15):
        while b15.b5:
            b15 = b15.b5
        return b15
    def fonk20(self, b2):
        b16 = self.fonk18(self.b14, b2)
        if b16 is None:
            raise ValueError(f"Key {b2} not found in the tree.")
        if b16.fonk4():
            if b16.fonk5():
                self.b14 = None
            else:
                b16.b1.fonk2(b16)
        elif b16.b4 is None:
            self.fonk21(b16, b16.b5)
        elif b16.b5 is None:
            self.fonk21(b16, b16.b4)
        else:
            b17 = self.fonk19(b16.b4)
            if b17.b4:
                self.fonk21(b17, b17.b4)
            else:
                b17.b1.fonk2(b17)
            b16.b2 = b17.b2
            b16.b3 = b17.b3
        return b16.b3
    def fonk21(self, node_to_replace, new_node):
        if node_to_replace.fonk5():
            self.b14 = new_node
        else:
            node_to_replace.b1.fonk8(node_to_replace, new_node)
if b18 = = "__main__":
    b11 = class3()
    b11.fonk15(10, "ten")
    b11.fonk15(5, "five")
    b11.fonk15(15, "fifteen")
    b11.fonk15(7, "seven")
    b11.fonk15(3, "three")
    b19 = class2(b11)
    print("Tree in preorder (b12):")
    b19.fonk10(b12 = True)
    print(f"\nSearch for 7: {b11.fonk17(7)}")
    print("\nDeleting b15 with b2 5:")
    b11.fonk20(5)
    b19.fonk10(b12 = True)
    print(f"\nNumber of nodes: {b11.fonk13()}")