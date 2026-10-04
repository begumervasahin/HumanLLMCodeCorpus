class class1:
    class class2:
        def fonk1(self, b1, b2):
            self.b1 = b1
            self.b2 = b2
            self.b3 = None
            self.b4 = None
    def fonk2(self):
        self.b5 = None
        self.a1 = 0
        self.b6 = None
        self.b7 = "pre"
    def fonk3(self):
        self.b5 = None
        self.a1 = 0
        self.b6 = None
        self.b7 = "pre"
    def fonk4(self, b1, b2):
        self.b5 = self.fonk5(self.b5, b1, b2)
        self.a1 += 1
    def fonk5(self, node, b1, b2):
        if node is None:
            return class1.class2(b1, b2)
        if b1 < node.b1:
            node.b3 = self.fonk5(node.b3, b1, b2)
        else:
            node.b4 = self.fonk5(node.b4, b1, b2)
        return node
    def fonk6(self, b1):
        return self.fonk7(self.b5, b1)
    def fonk7(self, node, b1):
        if node is None:
            return None
        if b1 = = node.b1:
            return node.b2
        elif b1 < node.b1:
            return self.fonk7(node.b3, b1)
        else:
            return self.fonk7(node.b4, b1)
    def fonk8(self, b1):
        self.b6 = None
        self.b5 = self.fonk9(self.b5, b1)
        return self.b6
    def fonk9(self, node, b1):
        if node is None:
            return None
        if b1 = = node.b1:
            if node.b3 is None and node.b4 is None:
                self.b6 = node.b2
                self.a1 -= 1
                return None
            if node.b3 is None:
                self.b6 = node.b2
                self.a1 -= 1
                return node.b4
            if node.b4 is None:
                self.b6 = node.b2
                self.a1 -= 1
                return node.b3
            b8 = self.fonk10(node.b4)
            node.b1, node.b2 = b8.b1, b8.b2
            node.b4 = self.fonk9(node.b4, b8.b1)
            self.b6 = node.b2
            return node
        elif b1 < node.b1:
            node.b3 = self.fonk9(node.b3, b1)
        else:
            node.b4 = self.fonk9(node.b4, b1)
        return node
    def fonk10(self, node):
        b9 = node
        while b9.b3 is not None:
            b9 = b9.b3
        return b9
    def fonk11(self):
        self.b7 = "pre"
        return self
    def fonk12(self):
        self.b7 = "in"
        return self
    def fonk13(self):
        self.b7 = "post"
        return self
    def fonk14(self):
        return self.fonk15(self.b5)
    def fonk15(self, node):
        if node is None:
            return
        if self.b7 = = "pre":
            yield node.b2
        if node.b3:
            yield from self.fonk15(node.b3)
        if self.b7 = = "in":
            yield node.b2
        if node.b4:
            yield from self.fonk15(node.b4)
        if self.b7 = = "post":
            yield node.b2
    def fonk16(self):
        return self.a1