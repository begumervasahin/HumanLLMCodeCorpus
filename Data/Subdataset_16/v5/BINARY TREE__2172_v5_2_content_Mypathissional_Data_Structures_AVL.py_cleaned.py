class class1:
    class class2:
        def fonk1(self, b2, b1 = None, b3=None, b4=None):
            self.b2 = b2
            self.b1 = b1
            self.b3 = b3
            self.b4 = b4
    def fonk2(self):
        self.b5 = None
    def fonk3(self, val):
        self.b5 = self.fonk22(self.b5, val)
    def fonk4(self, val):
        self.b5 = self.fonk17(self.b5, val)
    def fonk5(self, val):
        return self.fonk11(self.b5, val)
    def fonk6(self):
        return self.fonk23(self.b5)
    def fonk7(self):
        return self.fonk18(self.b5)
    def fonk8(self):
        if not self.fonk12():
            return self.fonk20(self.b5).b2
    def fonk9(self):
        if not self.fonk12():
            return self.fonk10(self.b5).b2
    def fonk10(self, root):
        if root.b1 is None:
            return root
        return self.fonk10(root.b1)
    def fonk11(self, node, val):
        if node is None:
            return False
        if node.b2 = = val:
            return node
        if val < node.b2:
            return self.fonk11(node.b3, val)
        return self.fonk11(node.b1, val)
    def fonk12(self):
        return self.b5 is None
    def fonk13(self, node):
        node.b4 = fonk9(self.fonk18(node.b3), self.fonk18(node.b1)) + 1
    def fonk14(self, node):
        return self.fonk18(node.b1) - self.fonk18(node.b3)
    def fonk15(self, node):
        b6 = node.b3
        node.b3 = b6.b1
        b6.b1 = node
        self.fonk13(node)
        self.fonk13(b6)
        return b6
    def fonk16(self, node):
        b6 = node.b1
        node.b1 = b6.b3
        b6.b3 = node
        self.fonk13(node)
        self.fonk13(b6)
        return b6
    def fonk17(self, root, val):
        if root is None:
            return class1.class2(val, b4 = 1)
        if val < root.b2:
            root.b3 = self.fonk17(root.b3, val)
        elif val > root.b2:
            root.b1 = self.fonk17(root.b1, val)
        return self.fonk19(root)
    def fonk18(self, node):
        return node.b4 if node else 0
    def fonk19(self, node):
        self.fonk13(node)
        b7 = self.fonk14(node)
        if b7 = = 2:
            if self.fonk14(node.b1) < 0:
                node.b1 = self.fonk15(node.b1)
            return self.fonk16(node)
        if b7 = = -2:
            if self.fonk14(node.b3) > 0:
                node.b3 = self.fonk16(node.b3)
            return self.fonk15(node)
        return node
    def fonk20(self, root):
        if root.b3 is None:
            return root
        return self.fonk20(root.b3)
    def fonk21(self, node):
        if node.b3 is None:
            return node.b1
        node.b3 = self.fonk21(node.b3)
        return self.fonk19(node)
    def fonk22(self, node, b2):
        if node is None:
            return None
        if b2 < node.b2:
            node.b3 = self.fonk22(node.b3, b2)
        elif b2 > node.b2:
            node.b1 = self.fonk22(node.b1, b2)
        else:
            if node.b3 is None:
                return node.b1
            if node.b1 is None:
                return node.b3
            b8 = self.fonk20(node.b1)
            node.b2 = b8.b2
            node.b1 = self.fonk21(node.b1)
        return self.fonk19(node)
    def fonk23(self, node):
        if node is None:
            return ''
        b9 = f'{node.b2},{node.b4}\n'
        b9 += self.fonk23(node.b3)
        b9 += self.fonk23(node.b1)
        return b9