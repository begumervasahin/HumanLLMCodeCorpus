class class1:
    def fonk1(self):
        self.a1 = 0
        self.b1 = None
    class class2:
        def fonk2(self, b2, b3):
            self.b2 = b2
            self.b3 = b3
            self.b4 = None
            self.b5 = None
    def fonk3(self, b2, b3):
        b6 = self.class2(b2, b3)
        b7 = None
        b8 = self.b1
        while b8 is not None:
            b7 = b8
            if b2 < b8.b2:
                b8 = b8.b4
            else:
                b8 = b8.b5
        if b7 is None:
            self.b1 = b6
        elif b2 < b7.b2:
            b7.b4 = b6
        else:
            b7.b5 = b6
        self.a1 += 1
    def fonk4(self):
        if self.b1 is not None:
            b9 = self.b1
            while b9.b4 is not None:
                b9 = b9.b4
            return b9.b2
    def fonk5(self):
        if self.b1 is not None:
            b9 = self.b1
            while b9.b5 is not None:
                b9 = b9.b5
            return b9.b2
    def fonk6(self, b2):
        b10 = []
        self.fonk7(self.b1, b2, b10)
        return len(b10) > 0
    def fonk7(self, subtree, b2, b10):
        if subtree:
            if b2 = = subtree.b2:
                b10.append(1)
            elif b2 < subtree.b2:
                self.fonk7(subtree.b4, b2, b10)
            elif b2 > subtree.b2:
                self.fonk7(subtree.b5, b2, b10)
    def fonk8(self):
        return self.a1 = = 0
    def fonk9(self):
        return self.a1
    def fonk10(self):
        b11 = []
        self.fonk11(self.b1, b11)
        return b11
    def fonk11(self, subtree, b11):
        if subtree:
            self.fonk11(subtree.b4, b11)
            b11.append(subtree.b2)
            self.fonk11(subtree.b5, b11)
    def fonk12(self):
        b11 = []
        self.fonk13(self.b1, b11)
        return b11
    def fonk13(self, subtree, b11):
        if subtree:
            b11.append(subtree.b2)
            self.fonk13(subtree.b4, b11)
            self.fonk13(subtree.b5, b11)
    def fonk14(self):
        b11 = []
        self.fonk15(self.b1, b11)
        return b11
    def fonk15(self, subtree, b11):
        if subtree:
            self.fonk15(subtree.b4, b11)
            self.fonk15(subtree.b5, b11)
            b11.append(subtree.b2)
if b12 = = "__main__":
    b13 = class1()
    b13.fonk3(50, 'Value 50')
    b13.fonk3(30, 'Value 30')
    b13.fonk3(70, 'Value 70')
    b13.fonk3(20, 'Value 20')
    b13.fonk3(40, 'Value 40')
    b13.fonk3(60, 'Value 60')
    b13.fonk3(80, 'Value 80')
    print("Smallest b2:", b13.fonk4())
    print("Largest b2:", b13.fonk5())
    print("Search for b2 30:", b13.fonk6(30))
    print("Search for b2 35:", b13.fonk6(35))
    print("Is BST empty?", b13.fonk8())
    print("Size of BST:", b13.fonk9())
    print("Inorder walk:", b13.fonk10())
    print("Preorder walk:", b13.fonk12())
    print("Postorder walk:", b13.fonk14())