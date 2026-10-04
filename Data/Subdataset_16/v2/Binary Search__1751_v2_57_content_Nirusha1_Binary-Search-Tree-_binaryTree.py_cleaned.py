class class1:
    class class2:
        def fonk1(self, b1, b2):
            self.b1 = b1
            self.b2 = b2
            self.b3 = None
            self.b4 = None
    def fonk2(self):
        self.a1 = 0
        self.b5 = None
    def fonk3(self, b1, b2):
        b6 = self.class2(b1, b2)
        b7 = None
        b8 = self.b5
        while b8 is not None:
            b7 = b8
            if b1 < b8.b1:
                b8 = b8.b3
            else:
                b8 = b8.b4
        if b7 is None:
            self.b5 = b6
        elif b1 < b7.b1:
            b7.b3 = b6
        else:
            b7.b4 = b6
        self.a1 += 1
    def fonk4(self):
        if self.b5 is not None:
            b8 = self.b5
            while b8.b3 is not None:
                b8 = b8.b3
            return b8.b1
        return None
    def fonk5(self):
        if self.b5 is not None:
            b8 = self.b5
            while b8.b4 is not None:
                b8 = b8.b4
            return b8.b1
        return None
    def fonk6(self, b1):
        return self.fonk7(self.b5, b1)
    def fonk7(self, subtree, b1):
        if subtree is None:
            return False
        if b1 = = subtree.b1:
            return True
        elif b1 < subtree.b1:
            return self.fonk7(subtree.b3, b1)
        else:
            return self.fonk7(subtree.b4, b1)
    def fonk8(self):
        return self.a1 = = 0
    def fonk9(self):
        return self.a1
    def fonk10(self):
        b9 = []
        self.fonk11(self.b5, b9)
        return b9
    def fonk11(self, subtree, b9):
        if subtree is not None:
            self.fonk11(subtree.b3, b9)
            b9.append(subtree.b1)
            self.fonk11(subtree.b4, b9)
    def fonk12(self):
        b9 = []
        self.fonk13(self.b5, b9)
        return b9
    def fonk13(self, subtree, b9):
        if subtree is not None:
            b9.append(subtree.b1)
            self.fonk13(subtree.b3, b9)
            self.fonk13(subtree.b4, b9)
    def fonk14(self):
        b9 = []
        self.fonk15(self.b5, b9)
        return b9
    def fonk15(self, subtree, b9):
        if subtree is not None:
            self.fonk15(subtree.b3, b9)
            self.fonk15(subtree.b4, b9)
            b9.append(subtree.b1)
if b10 = = "__main__":
    b11 = class1()
    b11.fonk3(10, "Ten")
    b11.fonk3(20, "Twenty")
    b11.fonk3(5, "Five")
    b11.fonk3(7, "Seven")
    b11.fonk3(30, "Thirty")
    print("Smallest b1:", b11.fonk4())
    print("Largest b1:", b11.fonk5())
    print("Search for b1 20:", b11.fonk6(20))
    print("Search for b1 15:", b11.fonk6(15))
    print("Inorder traversal:", b11.fonk10())
    print("Preorder traversal:", b11.fonk12())
    print("Postorder traversal:", b11.fonk14())
    print("Is the BST empty?", b11.fonk8())
    print("Size of the BST:", b11.fonk9())