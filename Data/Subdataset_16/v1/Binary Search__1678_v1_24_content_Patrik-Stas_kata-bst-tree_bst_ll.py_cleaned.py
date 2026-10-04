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
        print(f"class1({self.b2})  {b7}  {b8} {b9}")
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
            raise Exception("b10 b15 not found")
        b10.b1 = None
class class2:
    def fonk9(self, b11):
        self.b11 = b11
    def fonk10(self, b12 = False):
        self.fonk11(self.b11.b14, b12)
    def fonk11(self, traverse_node, b12):
        if traverse_node is None:
            raise Exception("Passing None as b15 to preorder print is not expected.")
        if b12:
            traverse_node.fonk3()
        else:
            print(f"{traverse_node.b2} ", b13 = "")
        if traverse_node.b4 is not None:
            self.fonk11(traverse_node.b4, b12)
        if traverse_node.b5 is not None:
            self.fonk11(traverse_node.b5, b12)
class class3:
    def fonk12(self):
        self.b14 = None
    def fonk13(self):
        return self.fonk14(self.b14)
    def fonk14(self, subtree_root):
        if subtree_root is not None:
            return 1 + self.fonk14(subtree_root.b4) + self.fonk14(subtree_root.b5)
        else:
            return 0
    def fonk15(self, b3, b2):
        if b3 is None or b2 is None:
            raise Exception("Insert b3 or b2 is null.")
        elif self.b14 is None:
            self.b14 = class1(b3, b2, b1=None)
        else:
            self.fonk16(self.b14, b3, b2)
    def fonk16(self, subtree_root, b3, b2):
        if subtree_root.b3 = = b3:
            raise Exception(f"Duplicate b3 {b3}")
        else:
            if b3 < subtree_root.b3:
                if subtree_root.b4 is None:
                    subtree_root.fonk7(class1(b3, b2))
                else:
                    self.fonk16(subtree_root.b4, b3, b2)
            else:
                if subtree_root.b5 is None:
                    subtree_root.fonk6(class1(b3, b2))
                else:
                    self.fonk16(subtree_root.b5, b3, b2)
    def fonk17(self, subtree_root, search_key):
        if subtree_root is None:
            return None
        if subtree_root.b3 = = search_key:
            return subtree_root
        elif search_key < subtree_root.b3:
            return self.fonk17(subtree_root.b4, search_key)
        else:
            return self.fonk17(subtree_root.b5, search_key)
    def fonk18(self, search_key):
        b15 = self.fonk17(self.b14, search_key)
        return b15.b2 if b15 is not None else None
    def fonk19(self, subtree_root):
        if subtree_root.b5 is None:
            return subtree_root
        else:
            return self.fonk19(subtree_root.b5)
    def fonk20(self, key_delete):
        b16 = self.fonk17(self.b14, key_delete)
        if b16 is None:
            raise Exception(f"Can't delete b15 with b3 {key_delete} because it was not found in the tree.")
        b17 = b16.b2
        if b16.fonk4():
            if b16.fonk5():
                self.b14 = None
            else:
                b16.b1.fonk2(b16)
        elif b16.b4 is None:
            b16.b1.fonk8(b16, b16.b5)
        else:
            b18 = self.fonk19(b16.b4)
            if b18.b4 is not None:
                b18.b1.fonk8(b18, b18.b4)
            else:
                b18.b1.fonk2(b18)
            b16.b3 = b18.b3
            b16.b2 = b18.b2
        return b17
if b19 = = "__main__":
    b11 = class3()
    b11.fonk15(10, "ten")
    b11.fonk15(5, "five")
    b11.fonk15(15, "fifteen")
    b11.fonk15(7, "seven")
    b11.fonk15(3, "three")
    b20 = class2(b11)
    b20.fonk10(b12 = True)
    print(f"Search for 7: {b11.fonk18(7)}")
    b11.fonk20(5)
    b20.fonk10(b12 = True)
    print(f"Number of nodes: {b11.fonk13()}")