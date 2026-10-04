class class1:
    def fonk1(self):
        self.a1 = 0
        self.b1 = None
    class class2:
        def fonk2(self, b2, b3):
            self.b2 = b2
            self.b3 = b3
            self.b4 = None
            self.b5 = None
    def fonk3(self, b2, b3):
        b6 = self.class2(b2, b3)
        b7 = None
        b8 = self.b1
        while b8 is not None:
            b7 = b8
            if b2 < b8.b2:
                b8 = b8.b4
            else:
                b8 = b8.b5
        if b7 is None:
            self.b1 = b6
        elif b2 < b7.b2:
            b7.b4 = b6
        else:
            b7.b5 = b6
        self.a1 += 1
    def fonk4(self):
        if self.b1 is not None:
            b8 = self.b1
            while b8.b4 is not None:
                b8 = b8.b4
            return b8.b2
        return None
    def fonk5(self):
        if self.b1 is not None:
            b8 = self.b1
            while b8.b5 is not None:
                b8 = b8.b5
            return b8.b2
        return None
    def fonk6(self, b2):
        b9 = []
        self.fonk7(self.b1, b2, b9)
        return b9
    def fonk7(self, subtree, b2, b9):
        if subtree:
            if b2 = = subtree.b2:
                b9.append(subtree.b3)
            elif b2 < subtree.b2:
                self.fonk7(subtree.b4, b2, b9)
            else:
                self.fonk7(subtree.b5, b2, b9)
    def fonk8(self):
        return self.a1 = = 0
    def fonk9(self):
        return self.a1
    def fonk10(self):
        b10 = []
        self.fonk11(self.b1, b10)
        return b10
    def fonk11(self, subtree, b10):
        if subtree:
            self.fonk11(subtree.b4, b10)
            b10.append(subtree.b2)
            self.fonk11(subtree.b5, b10)
    def fonk12(self):
        b10 = []
        self.fonk13(self.b1, b10)
        return b10
    def fonk13(self, subtree, b10):
        if subtree:
            b10.append(subtree.b2)
            self.fonk13(subtree.b4, b10)
            self.fonk13(subtree.b5, b10)
    def fonk14(self):
        b10 = []
        self.fonk15(self.b1, b10)
        return b10
    def fonk15(self, subtree, b10):
        if subtree:
            self.fonk15(subtree.b4, b10)
            self.fonk15(subtree.b5, b10)
            b10.append(subtree.b2)