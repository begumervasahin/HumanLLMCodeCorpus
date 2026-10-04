class class1:
    class class2:
        def fonk1(self, b2, b1 = None, b3=None, b4=1):
            self.b2 = b2
            self.b1 = b1
            self.b3 = b3
            self.b4 = b4
    def fonk2(self):
        self.b5 = None
    def fonk3(self, b2):
        self.b5 = self.fonk10(self.b5, b2)
    def fonk4(self, b2):
        self.b5 = self.fonk11(self.b5, b2)
    def fonk5(self, b2):
        return self.fonk21(self.b5, b2)
    def fonk6(self):
        return self.fonk17(self.b5)
    def fonk7(self):
        if not self.fonk9():
            return self.fonk18(self.b5).b2
    def fonk8(self):
        if not self.fonk9():
            return self.fonk19(self.b5).b2
    def fonk9(self):
        return self.b5 is None
    def fonk10(self, node, b2):
        if node is None:
            return class1.class2(b2)
        if b2 < node.b2:
            node.b3 = self.fonk10(node.b3, b2)
        elif b2 > node.b2:
            node.b1 = self.fonk10(node.b1, b2)
        else:
            return node
        return self.fonk12(node)
    def fonk11(self, node, b2):
        if not node:
            return None
        if b2 < node.b2:
            node.b3 = self.fonk11(node.b3, b2)
        elif b2 > node.b2:
            node.b1 = self.fonk11(node.b1, b2)
        else:
            if node.b3 is None:
                return node.b1
            elif node.b1 is None:
                return node.b3
            b6 = self.fonk18(node.b1)
            node.b2 = b6.b2
            node.b1 = self.fonk20(node.b1)
        return self.fonk12(node)
    def fonk12(self, node):
        self.fonk15(node)
        if self.fonk16(node) == 2:
            if self.fonk16(node.b1) < 0:
                node.b1 = self.fonk14(node.b1)
            return self.fonk13(node)
        if self.fonk16(node) == -2:
            if self.fonk16(node.b3) > 0:
                node.b3 = self.fonk13(node.b3)
            return self.fonk14(node)
        return node
    def fonk13(self, node):
        b7 = node.b1
        node.b1 = b7.b3
        b7.b3 = node
        self.fonk15(node)
        self.fonk15(b7)
        return b7
    def fonk14(self, node):
        b7 = node.b3
        node.b3 = b7.b1
        b7.b1 = node
        self.fonk15(node)
        self.fonk15(b7)
        return b7
    def fonk15(self, node):
        node.b4 = fonk8(self.fonk17(node.b3), self.fonk17(node.b1)) + 1
    def fonk16(self, node):
        return self.fonk17(node.b1) - self.fonk17(node.b3)
    def fonk17(self, node):
        return node.b4 if node else 0
    def fonk18(self, node):
        return node if node.b3 is None else self.fonk18(node.b3)
    def fonk19(self, node):
        return node if node.b1 is None else self.fonk19(node.b1)
    def fonk20(self, node):
        if node.b3 is None:
            return node.b1
        node.b3 = self.fonk20(node.b3)
        return self.fonk12(node)
    def fonk21(self, node, b2):
        if node is None:
            return None
        if node.b2 = = b2:
            return node
        elif b2 < node.b2:
            return self.fonk21(node.b3, b2)
        else:
            return self.fonk21(node.b1, b2)
    def fonk22(self):
        return self.fonk23(self.b5)
    def fonk23(self, node):
        if node is None:
            return ''
        b8 = f'{node.b2},{node.b4}\n'
        b8 += self.fonk23(node.b3)
        b8 += self.fonk23(node.b1)
        return b8