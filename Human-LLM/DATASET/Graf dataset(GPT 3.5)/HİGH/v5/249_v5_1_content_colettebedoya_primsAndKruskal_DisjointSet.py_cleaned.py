class class1:
    def fonk1(self, b1):
        if b1 < 0:
            raise ValueError("Size must be >= 0")
        self.b1 = b1
        self.b2 = [-1] * (b1 + 1)
    def fonk2(self, root1, root2):
        if not self.fonk4(root1) or not self.fonk4(root2):
            raise ValueError("Invalid root value")
        self.b2[root2] = root1
    def fonk3(self, root):
        if not self.fonk4(root):
            raise ValueError("Invalid root value")
        if self.b2[root] < 0:
            return root
        else:
            return self.fonk3(self.b2[root])
    def fonk4(self, root):
        return 0 <= root <= self.b1