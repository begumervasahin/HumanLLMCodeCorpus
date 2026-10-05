class class1:
    def fonk1(self, b1):
        if b1 < 0:
            raise ValueError("Size must be >= 0")
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