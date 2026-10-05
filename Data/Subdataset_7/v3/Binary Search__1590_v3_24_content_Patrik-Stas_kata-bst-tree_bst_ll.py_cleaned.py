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
    def fonk6(self, b6):
        self.b5 = b6
        b6.b1 = self
    def fonk7(self, b6):
        self.b4 = b6
        b6.b1 = self
    def fonk8(self, b10, new_child):
        if b10 = = self.b4:
            self.fonk7(new_child)
        elif b10 = = self.b5:
            self.fonk6(new_child)
        else:
            raise ValueError("b10 b13 not found")
class class2:
    def fonk9(self):
        self.b11 = None
    def fonk10(self):
        return self.fonk11(self.b11)
    def fonk11(self, b12):
        if b12:
            return 1 + self.fonk11(b12.b4) + self.fonk11(b12.b5)
        return 0
    def fonk12(self, b2, b3):
        if b2 is None or b3 is None:
            raise ValueError("Key or b3 cannot be None.")
        if not self.b11:
            self.b11 = class1(b2, b3)
        else:
            self.fonk13(self.b11, b2, b3)
    def fonk13(self, b12, b2, b3):
        if b2 = = b12.b2:
            raise ValueError("Duplicate b2: " + str(b2))
        elif b2 < b12.b2:
            if not b12.b4:
                b12.fonk7(class1(b2, b3))
            else:
                self.fonk13(b12.b4, b2, b3)
        else:
            if not b12.b5:
                b12.fonk6(class1(b2, b3))
            else:
                self.fonk13(b12.b5, b2, b3)
    def fonk14(self, search_key):
        return self.fonk15(self.b11, search_key)
    def fonk15(self, b12, search_key):
        if not b12 or b12.b2 = = search_key:
            return b12
        if search_key < b12.b2:
            return self.fonk15(b12.b4, search_key)
        return self.fonk15(b12.b5, search_key)
    def fonk16(self, b12):
        while b12.b5:
            b12 = b12.b5
        return b12
    def fonk17(self, b2):
        b13 = self.fonk14(b2)
        if not b13:
            raise ValueError(f"class1 with b2 {b2} not found.")
        if b13.fonk4():
            if b13.b1:
                b13.b1.fonk2(b13)
            else:
                self.b11 = None
        elif not b13.b4:
            b13.b1.fonk8(b13, b13.b5)
        elif not b13.b5:
            b13.b1.fonk8(b13, b13.b4)
        else:
            b14 = self.fonk16(b13.b4)
            b13.b2, b13.b3 = b14.b2, b14.b3
            self.fonk17(b14.b2)
class class3:
    def fonk18(self, b15):
        self.b15 = b15
    def fonk19(self):
        self.fonk20(self.b15.b11)
    def fonk20(self, b13):
        if b13:
            b13.fonk3()
            self.fonk20(b13.b4)
            self.fonk20(b13.b5)
if b16 = = "__main__":
    b15 = class2()
    b15.fonk12(10, "A")
    b15.fonk12(5, "B")
    b15.fonk12(15, "C")
    b15.fonk12(3, "D")
    b15.fonk12(7, "E")
    b15.fonk12(12, "F")
    b15.fonk12(17, "G")
    b17 = class3(b15)
    b17.fonk19()
