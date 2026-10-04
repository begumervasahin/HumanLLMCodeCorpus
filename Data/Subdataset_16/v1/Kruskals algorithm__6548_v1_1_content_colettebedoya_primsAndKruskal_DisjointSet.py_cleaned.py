class class1:
    def fonk1(self, b1):
        if b1 < 0:
            raise ValueError("b1 must be >= 0")
        self.b1 = b1
        self.b2 = [-1] * (b1 + 1)
    def fonk2(self, root1, root2):
        if root1 < 0 or root1 > self.b1 or root2 < 0 or root2 > self.b1:
            raise ValueError("Illegal value")
        b3 = self.fonk3(root1)
        b4 = self.fonk3(root2)
        if b3 != b4:
            self.b2[b4] = b3
    def fonk3(self, root):
        if root < 0 or root > self.b1:
            raise ValueError("Illegal value")
        if self.b2[root] < 0:
            return root
        else:
            self.b2[root] = self.fonk3(self.b2[root])
            return self.b2[root]
if b5 = = "__main__":
    b6 = class1(10)
    b6.fonk2(1, 2)
    b6.fonk2(3, 4)
    b6.fonk2(2, 3)
    print("Root of 1:", b6.fonk3(1))
    print("Root of 2:", b6.fonk3(2))
    print("Root of 3:", b6.fonk3(3))
    print("Root of 4:", b6.fonk3(4))
    try:
        print(b6.fonk3(11))
    except ValueError as e:
        print(e)