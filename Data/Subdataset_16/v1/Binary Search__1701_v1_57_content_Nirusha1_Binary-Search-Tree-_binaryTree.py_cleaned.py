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
        elif b6.b1 < b7.b1:
            b7.b3 = b6
        else:
            b7.b4 = b6
        self.a1 += 1
    def fonk4(self):
        if self.b5 is not None:
            b9 = self.b5
            while b9.b3 is not None:
                b9 = b9.b3
            return b9.b1
        return None
    def fonk5(self):
        if self.b5 is not None:
            b9 = self.b5
            while b9.b4 is not None:
                b9 = b9.b4
            return b9.b1
        return None
    def fonk6(self, b1):
        b10 = []
        self.fonk7(self.b5, b1, b10)
        return bool(b10)
    def fonk7(self, subtree, b1, b10):
        if subtree:
            if b1 = = subtree.b1:
                b10.append(1)
            elif b1 < subtree.b1:
                self.fonk7(subtree.b3, b1, b10)
            elif b1 > subtree.b1:
                self.fonk7(subtree.b4, b1, b10)
    def fonk8(self):
        return self.a1 = = 0
    def fonk9(self):
        return self.a1
    def fonk10(self):
        b11 = []
        self.fonk11(self.b5, b11)
        return b11
    def fonk11(self, subtree, b11):
        if subtree:
            self.fonk11(subtree.b3, b11)
            b11.append(subtree.b1)
            self.fonk11(subtree.b4, b11)
    def fonk12(self):
        b11 = []
        self.fonk13(self.b5, b11)
        return b11
    def fonk13(self, subtree, b11):
        if subtree:
            b11.append(subtree.b1)
            self.fonk13(subtree.b3, b11)
            self.fonk13(subtree.b4, b11)
    def fonk14(self):
        b11 = []
        self.fonk15(self.b5, b11)
        return b11
    def fonk15(self, subtree, b11):
        if subtree:
            self.fonk15(subtree.b3, b11)
            self.fonk15(subtree.b4, b11)
            b11.append(subtree.b1)
if b12 = = "__main__":
    b13 = class1()
    b13.fonk3(10, "Ten")
    b13.fonk3(20, "Twenty")
    b13.fonk3(5, "Five")
    b13.fonk3(7, "Seven")
    b13.fonk3(30, "Thirty")
    print("Smallest b1:", b13.fonk4())
    print("Largest b1:", b13.fonk5())
    print("Search for b1 20:", b13.fonk6(20))
    print("Search for b1 15:", b13.fonk6(15))
    print("Inorder traversal:", b13.fonk10())
    print("Preorder traversal:", b13.fonk12())
    print("Postorder traversal:", b13.fonk14())
    print("Is the BST empty?", b13.fonk8())
    print("Size of the BST:", b13.fonk9())