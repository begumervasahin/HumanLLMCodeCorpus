class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
        self.b4 = None
        self.b5 = None
        self.b6 = None
    def fonk2(self, node):
        if node:
            self.fonk2(node.b2)
            print(node.b1, b7 = ' ')
            self.fonk2(node.b3)
    def fonk3(self, node):
        if not node:
            return
        if node.b2:
            self.fonk3(node.b2)
        if not self.b4:
            if self.b6 and node.b1 < self.b6.b1:
                self.b4 = self.b6
                self.b5 = node
        else:
            if self.b5:
                if node.b1 < self.b5.b1:
                    self.b5 = node
        self.b6 = node
        if node.b3:
            self.fonk3(node.b3)
    def fonk4(self, root):
        self.fonk3(root)
        if self.b4 and self.b5:
            self.b4.b1, self.b5.b1 = self.b5.b1, self.b4.b1
b8 = class1(7)
b8.b2 = class1(4)
b8.b2.b2 = class1(1)
b8.b2.b3 = class1(5)
b8.b3 = class1(11)
b8.b1, b8.b2.b2.b1 = b8.b2.b2.b1, b8.b1
print("In-order traversal before fixing the swap:")
b8.fonk2(b8)
print()
b8.fonk4(b8)
print("In-order traversal after fixing the swap:")
b8.fonk2(b8)
print()