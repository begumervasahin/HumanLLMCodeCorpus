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
            print(node.b1)
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
        self.b4.b1, self.b5.b1 = self.b5.b1, self.b4.b1
b7 = class1(7)
b7.b2 = class1(4)
b7.b2.b2 = class1(1)
b7.b2.b3 = class1(5)
b7.b3 = class1(11)
b7.b1, b7.b2.b2.b1 = b7.b2.b2.b1, b7.b1
print("In-order traversal before swapping:")
b7.fonk2(b7)
print("\nIn-order traversal after swapping:")
b7.fonk4(b7)
b7.fonk2(b7)