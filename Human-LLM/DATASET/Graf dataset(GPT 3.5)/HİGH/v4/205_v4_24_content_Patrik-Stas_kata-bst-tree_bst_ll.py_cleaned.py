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
        b7 = "        " if self.b4 is None else f"_left: {self.b4.b3}"
        b8 = "         " if self.b5 is None else f"_right: {self.b5.b3}"
        b9 = "   ROOT" if self.b1 is None else f"   _parent: {self.b1.b3}"
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
            raise ValueError("b10 b15 not found")
class class2:
    def fonk9(self, b11):
        self.b11 = b11
    def fonk10(self):
        print("foo")
    def fonk11(self, b12 = False):
        self.fonk12(self.b11.b14, b12)
    def fonk12(self, traverse_node, b12):
        if traverse_node is None:
            raise ValueError("Passing None as b15 to preorder print is not expected.")
        if b12:
            traverse_node.fonk3()
        else:
            print(str(traverse_node.b3) + " ", b13 = '')
        if traverse_node.b4 is not None:
            self.fonk12(traverse_node.b4, b12)
        if traverse_node.b5 is not None:
            self.fonk12(traverse_node.b5, b12)
class class3:
    def fonk13(self):
        self.b14 = None
    def fonk14(self):
        return self.fonk15(self.b14)
    def fonk15(self, subtree_root):
        if subtree_root is not None:
            return 1 + self.fonk15(subtree_root.b4) + self.fonk15(subtree_root.b5)
        return 0
    def fonk16(self, b2, b3):
        if b2 is None or b3 is None:
            raise ValueError("Insert b2 or b3 is null.")
        elif self.b14 is None:
            self.b14 = class1(b2, b3, b1=None)
        else:
            self.fonk17(self.b14, b2, b3)
    def fonk17(self, subtree_root, b2, b3):
        if subtree_root.b2 = = b2:
            raise ValueError("Duplicate b2 " + str(b2))
        else:
            if b2 < subtree_root.b2:
                if subtree_root.b4 is None:
                    subtree_root.fonk7(class1(b2, b3))
                else:
                    self.fonk17(subtree_root.b4, b2, b3)
            else:
                if subtree_root.b5 is None:
                    subtree_root.fonk6(class1(b2, b3))
                else:
                    self.fonk17(subtree_root.b5, b2, b3)
    def fonk18(self, subtree_root, search_key):
        if subtree_root is None:
            return None
        if subtree_root.b2 = = search_key:
            return subtree_root
        elif search_key < subtree_root.b2:
            return self.fonk18(subtree_root.b4, search_key)
        else:
            return self.fonk18(subtree_root.b5, search_key)
    def fonk19(self, search_key):
        b15 = self.fonk18(self.b14, search_key)
        return b15.b3 if b15 is not None else None
    def fonk20(self, subtree_root):
        if subtree_root.b5 is None:
            return subtree_root
        else:
            return self.fonk20(subtree_root.b5)
    def fonk21(self, key_delete):
        b16 = self.fonk18(self.b14, key_delete)
        if b16 is None:
            raise ValueError("Can't delete b15 with b2 " + str(key_delete) + " because it was not found in the tree.")
        b17 = b16.b3
        if b16 is None:
            raise ValueError("Value " + str(key_delete) + " not found in the tree.")
        if b16.fonk4():
            b16.b1.fonk2(b16)
        elif b16.b4 is None:
            b16.b1.fonk8(b16, b16.b5)
        else:
            b18 = self.fonk20(b16.b4)
            if b18.b4 is not None:
                b18.b1.fonk8(b18, b18.b4)
            else:
                b18.b1.fonk2(b18)
            b16.b2 = b18.b2
            b16.b3 = b18.b3
        return b17