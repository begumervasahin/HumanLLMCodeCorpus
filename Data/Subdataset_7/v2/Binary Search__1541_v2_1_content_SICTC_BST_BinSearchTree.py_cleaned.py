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
    def fonk4(self, node, b1, b2):
        if not node:
            b8 = class1.class2(b1, b2)
            return b8
        if b1 < node.b1:
            node.b3 = self.fonk4(node.b3, b1, b2)
        else:
            node.b4 = self.fonk4(node.b4, b1, b2)
        return node
    def fonk5(self, b1, b2):
        self.b5 = self.fonk4(self.b5, b1, b2)
        self.a1 += 1
    def fonk6(self, node, b1):
        if not node:
            return None
        if b1 = = node.b1:
            return node.b2
        if b1 < node.b1:
            return self.fonk6(node.b3, b1)
        else:
            return self.fonk6(node.b4, b1)
    def fonk7(self, b1):
        return self.fonk6(self.b5, b1)
    def fonk8(self, node, b1):
        if not node:
            return None
        if b1 = = node.b1:
            if not node.b3 and not node.b4:
                self.b6 = node.b2
                self.a1 -= 1
                return None
            if not node.b4:
                self.b6 = node.b2
                self.a1 -= 1
                return node.b3
            if not node.b3:
                self.b6 = node.b2
                self.a1 -= 1
                return node.b4
            b9 = self.fonk10(node.b4)
            b10 = node.b2
            node.b1 = b9.b1
            node.b2 = b9.b2
            node.b4 = self.fonk8(node.b4, b9.b1)
            self.b6 = b10
            return node
        if b1 < node.b1:
            node.b3 = self.fonk8(node.b3, b1)
        else:
            node.b4 = self.fonk8(node.b4, b1)
        return node
    def fonk9(self, b1):
        self.b6 = None
        self.b5 = self.fonk8(self.b5, b1)
        return self.b6
    def fonk10(self, node):
        b11 = node
        while b11.b3:
            b11 = b11.b3
        return b11
    def fonk11(self):
        self.b7 = "pre"
    def fonk12(self):
        self.b7 = "in"
    def fonk13(self):
        self.b7 = "post"
    def fonk14(self):
        return self.fonk15(self.b5)
    def fonk15(self, node):
        if not node:
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
b12 = class1()
b12.fonk5(5, 'five')
b12.fonk5(3, 'three')
b12.fonk5(7, 'seven')
print("Inorder traversal:")
b12.fonk12()
for b2 in b12:
    print(b2)