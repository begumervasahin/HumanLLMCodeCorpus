class class1(Exception):
    pass
class class2(Exception):
    pass
class class3:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
class class4:
    def fonk2(self, b1, b2):
        self.a1 = 0
        self.b4 = class3(b1, b2, self)
        self.b5 = []
        self.b6 = None
    def fonk3(self, other_tree):
        if self.a1 != other_tree.a1:
            raise class1()
        if self.b4.b1 > other_tree.b4.b1:
            raise class1()
        self.b5.append(other_tree)
        other_tree.b6 = self
        self.a1 += 1
    def fonk4(self, newkey):
        b7 = self
        b7.b4.b1 = newkey
        b6 = b7.b6
        while b6 is not None and b7.b4.b1 < b6.b4.b1:
            b6.b4, b7.b4 = b7.b4, b6.b4
            b6.b4.b3 = b6
            b7.b4.b3 = b7
            b7 = b6
            b6 = b7.b6
        return b7
    def fonk5(self, b8 = 0):
        return (" " * b8 +
                f"a1: {self.a1} b1: {self.b4.b1} b2: {self.b4.b2}" +
                "\n" + "".join(child.fonk13(b8+2) for child in self.b5))
class class5:
    def fonk6(self, b9 = 1e300):
        self.b9 = b9
        self.b6 = self
        self.b10 = []
        self.a2 = 0
        self.b11 = self.b9
        self.b12 = self.b9
        self.a3 = -1
    def fonk7(self):
        return 2 ** len(self.b10) - 1
    def fonk8(self):
        while self.fonk7() < self.a2:
            self.b10.append(None)
    def fonk9(self, new_tree):
        self.a2 += 2 ** new_tree.a1
        self.fonk8()
        while self.b10[new_tree.a1] is not None:
            if self.b10[new_tree.a1].b4.b1 < new_tree.b4.b1:
                new_tree, self.b10[new_tree.a1] = self.b10[new_tree.a1], new_tree
            b13 = new_tree.a1
            new_tree.fonk3(self.b10[b13])
            self.b10[b13] = None
        self.b10[new_tree.a1] = new_tree
        if new_tree.b4.b1 <= self.b11:
            self.b11 = new_tree.b4.b1
            self.b12 = new_tree.b4.b2
            self.a3 = new_tree.a1
    def fonk10(self, b1, b2):
        b3 = class4(b1, b2)
        self.fonk9(b3)
        return b3.b4
    def fonk11(self):
        if not self:
            raise class2()
        b14 = self.b10[self.a3]
        self.b10[b14.a1] = None
        self.a2 -= 2 ** b14.a1
        for child in b14.b5:
            child.b6 = None
            self.fonk9(child)
        self.b11 = self.b9
        for b3 in self.b10:
            if b3 is not None:
                if b3.b4.b1 <= self.b11:
                    self.b11 = b3.b4.b1
                    self.b12 = b3.b4.b2
                    self.a3 = b3.a1
        return b14.b4
    def fonk12(self, b7, newkey):
        b15 = b7.b3.fonk4(newkey)
        self.b11 = self.b9
        for b3 in self.b10:
            if b3 is not None:
                if b3.b4.b1 <= self.b11:
                    self.b11 = b3.b4.b1
                    self.b12 = b3.b4.b2
                    self.a3 = b3.a1
        return b15
    def fonk13(self):
        b16 = f"a2: {self.a2} min: {str(self.b11)}\n"
        b16 += f"a3: {self.a3}\n"
        b16 += "".join("10"[b3 is None] for b3 in self.b10) + "\n"
        b16 += "".join(str(b3) for b3 in self.b10 if b3 is not None)
        return b16
def fonk14():
    b17 = class5()
    b17.fonk10(12, "a")
    b17.fonk10(5, "b")
    b17.fonk10(21, "c")
    b17.fonk10(8, "d")
    b18 = b17.fonk10(100, "e")
    print(b17)
    print("min b4: ", b17.b12)
    print("\n")
    b17.fonk11()
    print(b17)
    print("min b4: ", b17.b12)
    b17.fonk12(b18, 1)
    print(b17)
    b17.fonk11()
    print(b17)
if b19 = = '__main__':
    fonk14()