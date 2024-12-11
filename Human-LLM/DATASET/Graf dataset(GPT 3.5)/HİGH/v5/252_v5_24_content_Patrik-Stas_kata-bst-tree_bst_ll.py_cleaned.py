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
        b7 = f"_left: {self.b4.b3}" if self.b4 else "        "
        b8 = f"_right: {self.b5.b3}" if self.b5 else "         "
        b9 = "   ROOT" if self.b1 is None else f"   _parent: {self.b1.b3}"
        print(f"class1({self.b3})  {b7}  {b8}  {b9}")
    def fonk4(self):
        return self.b4 is None and self.b5 is None
    def fonk5(self):
        return self.b1 is None
    def fonk6(self, b6):
        self.b5 = b6
        if b6:
            b6.b1 = self
    def fonk7(self, b6):
        self.b4 = b6
        if b6:
            b6.b1 = self
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
            print(f"{traverse_node.b3} ", b13 = '')
        if traverse_node.b4:
            self.fonk12(traverse_node.b4, b12)
        if traverse_node.b5:
            self.fonk12(traverse_node.b5, b12)
class class3:
    def fonk13(self):
        self.b14 = None
    def fonk14(self):
        return self.fonk15(self.b14)
    def fonk15(self, b16):
        if b16 is not None:
            return 1 + self.fonk15(b16.b4) + self.fonk15(b16.b5)
        return 0
    def fonk16(self, b2, b3):
        if b2 is None or b3 is None:
            raise ValueError("Key or b3 cannot be None.")
        if self.b14 is None:
            self.b14 = class1(b2, b3)
        else:
            self.fonk17(self.b14, b2, b3)
    def fonk17(self, b16, b2, b3):
        if b2 = = b16.b2:
            raise ValueError(f"Duplicate b2: {b2}")
        if b2 < b16.b2:
            if b16.b4 is None:
                b16.fonk7(class1(b2, b3))
            else:
                self.fonk17(b16.b4, b2, b3)
        else:
            if b16.b5 is None:
                b16.fonk6(class1(b2, b3))
            else:
                self.fonk17(b16.b5, b2, b3)
    def fonk18(self, b16, search_key):
        if b16 is None or b16.b2 = = search_key:
            return b16
        elif search_key < b16.b2:
            return self.fonk18(b16.b4, search_key)
        else:
            return self.fonk18(b16.b5, search_key)
    def fonk19(self, search_key):
        b15 = self.fonk18(self.b14, search_key)
        return b15.b3 if b15 else None
    def fonk20(self, b16):
        while b16.b5:
            b16 = b16.b5
        return b16
    def fonk21(self, b2):
        b15 = self.fonk18(self.b14, b2)
        if not b15:
            raise ValueError(f"class1 with b2 {b2} not found.")
        b17 = b15.b3
        if b15.fonk4():
            if b15.b1:
                b15.b1.fonk2(b15)
            else:
                self.b14 = None
        elif not b15.b4:
            b15.b1.fonk8(b15, b15.b5)
        elif not b15.b5:
            b15.b1.fonk8(b15, b15.b4)
        else:
            b18 = self.fonk20(b15.b4)
            b15.b2, b15.b3 = b18.b2, b18.b3
            self.fonk21(b18.b2)
        return b17