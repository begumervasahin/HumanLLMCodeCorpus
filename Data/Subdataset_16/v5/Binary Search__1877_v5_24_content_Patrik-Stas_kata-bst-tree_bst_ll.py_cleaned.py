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
        b7 = "b4: None" if self.b4 is None else f"b4: {self.b4.b3}"
        b8 = "b5: None" if self.b5 is None else f"b5: {self.b5.b3}"
        b9 = "ROOT" if self.b1 is None else f"b1: {self.b1.b3}"
        print(f"class1({self.b3})  {b7}  {b8}  {b9}")
    def fonk4(self):
        return self.b4 is None and self.b5 is None
    def fonk5(self):
        return self.b1 is None
    def fonk6(self, child_node):
        self.b5 = child_node
        child_node.b1 = self
    def fonk7(self, child_node):
        self.b4 = child_node
        child_node.b1 = self
    def fonk8(self, b10, new_child):
        if b10 = = self.b4:
            self.fonk7(new_child)
        elif b10 = = self.b5:
            self.fonk6(new_child)
        else:
            raise ValueError("Child b15 not found among this b15's children.")
        b10.b1 = None
class class2:
    def fonk9(self, b11):
        self.b11 = b11
        self.a1 = 40
    def fonk10(self):
        print("Tree structure placeholder")
    def fonk11(self, b12 = False):
        self.fonk12(self.b11.b14, b12)
    def fonk12(self, b15, b12):
        if b15 is None:
            return
        if b12:
            b15.fonk3()
        else:
            print(f"{b15.b3} ", b13 = "")
        self.fonk12(b15.b4, b12)
        self.fonk12(b15.b5, b12)
class class3:
    def fonk13(self):
        self.b14 = None
    def fonk14(self):
        return self.fonk15(self.b14)
    def fonk15(self, subtree_root):
        if subtree_root is None:
            return 0
        return 1 + self.fonk15(subtree_root.b4) + self.fonk15(subtree_root.b5)
    def fonk16(self, b2, b3):
        if b2 is None or b3 is None:
            raise ValueError("Key and b3 must be provided.")
        if self.b14 is None:
            self.b14 = class1(b2, b3)
        else:
            self.fonk17(self.b14, b2, b3)
    def fonk17(self, subtree_root, b2, b3):
        if b2 = = subtree_root.b2:
            raise ValueError(f"Duplicate b2 {b2}")
        elif b2 < subtree_root.b2:
            if subtree_root.b4 is None:
                subtree_root.fonk7(class1(b2, b3, subtree_root))
            else:
                self.fonk17(subtree_root.b4, b2, b3)
        else:
            if subtree_root.b5 is None:
                subtree_root.fonk6(class1(b2, b3, subtree_root))
            else:
                self.fonk17(subtree_root.b5, b2, b3)
    def fonk18(self, b16):
        b15 = self.fonk19(self.b14, b16)
        return b15.b3 if b15 else None
    def fonk19(self, subtree_root, b16):
        if subtree_root is None or b16 = = subtree_root.b2:
            return subtree_root
        if b16 < subtree_root.b2:
            return self.fonk19(subtree_root.b4, b16)
        return self.fonk19(subtree_root.b5, b16)
    def fonk20(self, subtree_root):
        b17 = subtree_root
        while b17.b5:
            b17 = b17.b5
        return b17
    def fonk21(self, b2):
        b18 = self.fonk19(self.b14, b2)
        if b18 is None:
            raise ValueError(f"class1 with b2 {b2} not found in the tree.")
        if b18.fonk4():
            self.fonk22(b18)
        elif b18.b4 is None:
            self.fonk23(b18, b18.b5)
        elif b18.b5 is None:
            self.fonk23(b18, b18.b4)
        else:
            self.fonk24(b18)
        return b18.b3
    def fonk22(self, b15):
        if b15.fonk5():
            self.b14 = None
        else:
            b15.b1.fonk2(b15)
    def fonk23(self, b15, child):
        if b15.fonk5():
            self.b14 = child
        else:
            b15.b1.fonk8(b15, child)
    def fonk24(self, b15):
        b19 = self.fonk20(b15.b4)
        if b19.b4:
            b19.b1.fonk8(b19, b19.b4)
        else:
            b19.b1.fonk2(b19)
        b15.b2 = b19.b2
        b15.b3 = b19.b3