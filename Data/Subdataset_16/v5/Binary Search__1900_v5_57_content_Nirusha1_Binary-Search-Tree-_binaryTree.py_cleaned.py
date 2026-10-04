class class1:
    def fonk1(self):
        self.b1 = None
        self.a1 = 0
    class class2:
        def fonk2(self, b2, b3):
            self.b2 = b2
            self.b3 = b3
            self.b4 = None
            self.b5 = None
    def fonk3(self, b2, b3):
        b6 = self.class2(b2, b3)
        if self.b1 is None:
            self.b1 = b6
        else:
            b7 = self.b1
            while True:
                if b2 < b7.b2:
                    if b7.b4 is None:
                        b7.b4 = b6
                        break
                    b7 = b7.b4
                else:
                    if b7.b5 is None:
                        b7.b5 = b6
                        break
                    b7 = b7.b5
        self.a1 += 1
    def fonk4(self):
        if self.b1 is None:
            return None
        b7 = self.b1
        while b7.b4 is not None:
            b7 = b7.b4
        return b7.b2
    def fonk5(self):
        if self.b1 is None:
            return None
        b7 = self.b1
        while b7.b5 is not None:
            b7 = b7.b5
        return b7.b2
    def fonk6(self, b2):
        b8 = []
        b7 = self.b1
        while b7 is not None:
            if b2 = = b7.b2:
                b8.append(b7.b3)
            b7 = b7.b4 if b2 < b7.b2 else b7.b5
        return b8
    def fonk7(self):
        return self.a1 = = 0
    def fonk8(self):
        return self.a1
    def fonk9(self):
        b9 = []
        self.fonk10(self.b1, b9)
        return b9
    def fonk10(self, node, b9):
        if node is not None:
            self.fonk10(node.b4, b9)
            b9.append(node.b2)
            self.fonk10(node.b5, b9)
    def fonk11(self):
        b9 = []
        self.fonk12(self.b1, b9)
        return b9
    def fonk12(self, node, b9):
        if node is not None:
            b9.append(node.b2)
            self.fonk12(node.b4, b9)
            self.fonk12(node.b5, b9)
    def fonk13(self):
        b9 = []
        self.fonk14(self.b1, b9)
        return b9
    def fonk14(self, node, b9):
        if node is not None:
            self.fonk14(node.b4, b9)
            self.fonk14(node.b5, b9)
            b9.append(node.b2)