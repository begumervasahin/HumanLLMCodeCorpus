class class1:
    def fonk1(self, b1):
        if b1 < 0:
            raise ValueError("b1 must be >= 0")
        self.b1 = b1
        self.b2 = [-1] * (b1 + 1)
    def fonk2(self, root1, root2):
        if not (0 <= root1 <= self.b1) or not (0 <= root2 <= self.b1):
            raise ValueError("Illegal value")
        self.b2[root2] = root1
    def fonk3(self, root):
        if not (0 <= root <= self.b1):
            raise ValueError("Illegal value")
        if self.b2[root] < 0:
            return root
        else:
            return self.fonk3(self.b2[root])
if b3 = = "__main__":
    b4 = class1(10)
    b4.fonk2(1, 2)
    b4.fonk2(3, 4)
    print(b4.fonk3(2))
    print(b4.fonk3(4))
    b4.fonk2(1, 3)
    print(b4.fonk3(4))
