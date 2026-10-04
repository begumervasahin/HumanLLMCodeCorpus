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
    def fonk3(self, b1, b2):
        b6 = self.class2(b1, b2)
        if self.b5 is None:
            self.b5 = b6
        else:
            self.fonk4(self.b5, b6)
        self.a1 += 1
    def fonk4(self, b7, b6):
        if b6.b1 < b7.b1:
            if b7.b3 is None:
                b7.b3 = b6
            else:
                self.fonk4(b7.b3, b6)
        else:
            if b7.b4 is None:
                b7.b4 = b6
            else:
                self.fonk4(b7.b4, b6)
    def fonk5(self):
        if self.b5 is None:
            return None
        return self.fonk6(self.b5).b1
    def fonk6(self, node):
        b7 = node
        while b7.b3 is not None:
            b7 = b7.b3
        return b7
    def fonk7(self):
        if self.b5 is None:
            return None
        return self.fonk8(self.b5).b1
    def fonk8(self, node):
        b7 = node
        while b7.b4 is not None:
            b7 = b7.b4
        return b7
    def fonk9(self, b1):
        return self.fonk10(self.b5, b1)
    def fonk10(self, node, b1):
        if node is None:
            return False
        if b1 = = node.b1:
            return True
        elif b1 < node.b1:
            return self.fonk10(node.b3, b1)
        else:
            return self.fonk10(node.b4, b1)
    def fonk11(self):
        return self.a1 = = 0
    def fonk12(self):
        return self.a1
    def fonk13(self):
        b8 = []
        self.fonk14(self.b5, b8)
        return b8
    def fonk14(self, node, b8):
        if node is not None:
            self.fonk14(node.b3, b8)
            b8.append(node.b1)
            self.fonk14(node.b4, b8)
    def fonk15(self):
        b8 = []
        self.fonk16(self.b5, b8)
        return b8
    def fonk16(self, node, b8):
        if node is not None:
            b8.append(node.b1)
            self.fonk16(node.b3, b8)
            self.fonk16(node.b4, b8)
    def fonk17(self):
        b8 = []
        self.fonk18(self.b5, b8)
        return b8
    def fonk18(self, node, b8):
        if node is not None:
            self.fonk18(node.b3, b8)
            self.fonk18(node.b4, b8)
            b8.append(node.b1)
if b9 = = "__main__":
    b10 = class1()
    b10.fonk3(10, "Ten")
    b10.fonk3(20, "Twenty")
    b10.fonk3(5, "Five")
    b10.fonk3(7, "Seven")
    b10.fonk3(30, "Thirty")
    print("Smallest b1:", b10.fonk5())
    print("Largest b1:", b10.fonk7())
    print("Search for b1 20:", b10.fonk9(20))
    print("Search for b1 15:", b10.fonk9(15))
    print("Inorder traversal:", b10.fonk13())
    print("Preorder traversal:", b10.fonk15())
    print("Postorder traversal:", b10.fonk17())
    print("Is the BST empty?", b10.fonk11())
    print("Size of the BST:", b10.fonk12())