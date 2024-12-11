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
        if self.b5 is None:
            self.b5 = b6
        else:
            b7 = None
            b8 = self.b5
            while b8:
                b7 = b8
                if b1 < b8.b1:
                    b8 = b8.b3
                else:
                    b8 = b8.b4
            if b1 < b7.b1:
                b7.b3 = b6
            else:
                b7.b4 = b6
        self.a1 += 1
    def fonk4(self):
        b8 = self.b5
        while b8 and b8.b3:
            b8 = b8.b3
        return b8.b1 if b8 else None
    def fonk5(self):
        b8 = self.b5
        while b8 and b8.b4:
            b8 = b8.b4
        return b8.b1 if b8 else None
    def fonk6(self, b1):
        return self.fonk7(self.b5, b1)
    def fonk7(self, b6, b1):
        if b6 is None or b6.b1 = = b1:
            return True
        if b1 < b6.b1:
            return self.fonk7(b6.b3, b1)
        return self.fonk7(b6.b4, b1)
    def fonk8(self):
        return self.a1 = = 0
    def fonk9(self):
        return self.a1
    def fonk10(self):
        b9 = []
        self.fonk11(self.b5, b9)
        return b9
    def fonk11(self, b6, b9):
        if b6:
            self.fonk11(b6.b3, b9)
            b9.append(b6.b1)
            self.fonk11(b6.b4, b9)
    def fonk12(self):
        b9 = []
        self.fonk13(self.b5, b9)
        return b9
    def fonk13(self, b6, b9):
        if b6:
            b9.append(b6.b1)
            self.fonk13(b6.b3, b9)
            self.fonk13(b6.b4, b9)
    def fonk14(self):
        b9 = []
        self.fonk15(self.b5, b9)
        return b9
    def fonk15(self, b6, b9):
        if b6:
            self.fonk15(b6.b3, b9)
            self.fonk15(b6.b4, b9)
            b9.append(b6.b1)
if b10 = = "__main__":
    b11 = class1()
    b12 = [(50, 'Value 50'), (30, 'Value 30'), (70, 'Value 70'), (20, 'Value 20'),
                   (40, 'Value 40'), (60, 'Value 60'), (80, 'Value 80')]
    for b1, b2 in b12:
        b11.fonk3(b1, b2)
    print("Smallest b1:", b11.fonk4())
    print("Largest b1:", b11.fonk5())
    print("Search for b1 30:", b11.fonk6(30))
    print("Search for b1 35:", b11.fonk6(35))
    print("Is BST empty?", b11.fonk8())
    print("Size of BST:", b11.fonk9())
    print("Inorder walk:", b11.fonk10())
    print("Preorder walk:", b11.fonk12())
    print("Postorder walk:", b11.fonk14())