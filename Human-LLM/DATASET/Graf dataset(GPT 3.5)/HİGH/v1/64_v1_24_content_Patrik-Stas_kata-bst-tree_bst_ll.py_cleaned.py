class class1:
    def fonk1(self, b3, b2, b1 = None):
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
        b7 = "        " if self.b4 is None else "b4: " + str(self.b4.b2)
        b8 = "         " if self.b5 is None else "b5: " + str(self.b5.b2)
        b9 = "   ROOT" if self.b1 is None else "   b1 " + str(self.b1.b2)
        print("class1(" + str(self.b2) + ")  " + b7 + "  " + b8 + b9)
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
            raise Exception("b10 b12 not found")
class class2:
    def fonk9(self):
        self.b11 = None
    def fonk10(self):
        return self.fonk11(self.b11)
    def fonk11(self, subtree_root):
        if subtree_root is not None:
            return 1 + self.fonk11(subtree_root.b4) + self.fonk11(subtree_root.b5)
        else:
            return 0
    def fonk12(self, b3, b2):
        if b3 is None or b2 is None:
            raise Exception("Insert b3 or b2 is null.")
        elif self.b11 is None:
            self.b11 = class1(b3, b2, b1=None)
        else:
            self.fonk13(self.b11, b3, b2)
    def fonk13(self, subtree_root, b3, b2):
        if subtree_root.b3 = = b3:
            raise Exception("Duplicate b3 " + str(b3))
        else:
            if b3 < subtree_root.b3:
                if subtree_root.b4 is None:
                    subtree_root.fonk7(class1(b3, b2))
                else:
                    self.fonk13(subtree_root.b4, b3, b2)
            else:
                if subtree_root.b5 is None:
                    subtree_root.fonk6(class1(b3, b2))
                else:
                    self.fonk13(subtree_root.b5, b3, b2)
    def fonk14(self, subtree_root, search_key):
        if subtree_root is None:
            return None
        if subtree_root.b3 = = search_key:
            return subtree_root
        elif search_key < subtree_root.b3:
            return self.fonk14(subtree_root.b4, search_key)
        else:
            return self.fonk14(subtree_root.b5, search_key)
    def fonk15(self, search_key):
        b12 = self.fonk14(self.b11, search_key)
        return b12.b2 if b12 is not None else None
    def fonk16(self, subtree_root):
        if subtree_root.b5 is None:
            return subtree_root
        else:
            return self.fonk16(subtree_root.b5)
    def fonk17(self, key_delete):
        b13 = self.fonk14(self.b11, key_delete)
        if b13 is None:
            raise Exception("Can't delete b12 with b3 " + str(key_delete) + " because it was not found in the tree.")
        b14 = b13.b2
        if b13 is None:
            raise Exception("Value " + str(key_delete) + " not found in the tree.")
        if b13.fonk4():
            b13.b1.fonk2(b13)
        elif b13.b4 is None:
            b13.b1.fonk8(b13, b13.b5)
        else:
            b15 = self.fonk16(b13.b4)
            if b15.b4 is not None:
                b15.b1.fonk8(b15, b15.b4)
            else:
                b15.b1.fonk2(b15)
            b13.b3 = b15.b3
            b13.b2 = b15.b2
        return b14
class class3:
    def fonk18(self, b16):
        self.b16 = b16
        self.a1 = 40
    def fonk19(self):
        print("foo")
    def fonk20(self, b17 = False):
        self.fonk21(self.b16.b11, b17)
    def fonk21(self, traverse_node, b17):
        if traverse_node is None:
            raise Exception("Passing None as b12 to preorder print is not expected.")
        if b17:
            traverse_node.fonk3()
        else:
            print(str(traverse_node.b2) + " ", b18 = '')
        if traverse_node.b4 is not None:
            self.fonk21(traverse_node.b4, b17)
        if traverse_node.b5 is not None:
            self.fonk21(traverse_node.b5, b17)
if b19 = = "__main__":
    b16 = class2()
    b16.fonk12(10, "A")
    b16.fonk12(5, "B")
    b16.fonk12(15, "C")
    b16.fonk12(3, "D")
    b16.fonk12(7, "E")
    b16.fonk12(12, "F")
    b16.fonk12(17, "G")
    b20 = class3(b16)
    b20.fonk20()
