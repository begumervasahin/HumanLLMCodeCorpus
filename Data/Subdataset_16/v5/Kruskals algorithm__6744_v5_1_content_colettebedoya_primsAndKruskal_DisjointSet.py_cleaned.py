class class1:
    def fonk1(self, b1):
        if b1 < 0:
            raise ValueError("Size must be >= 0")
        self.b1 = b1
        self.b2 = [-1] * (b1 + 1)
    def fonk2(self, b3, b4):
        if not (0 <= b3 <= self.b1) or not (0 <= b4 <= self.b1):
            raise ValueError("Invalid root value")
        b3 = self.fonk3(b3)
        b4 = self.fonk3(b4)
        if b3 != b4:
            self.b2[b4] = b3
    def fonk3(self, root):
        if not (0 <= root <= self.b1):
            raise ValueError("Invalid root value")
        if self.b2[root] < 0:
            return root
        else:
            self.b2[root] = self.fonk3(self.b2[root])
            return self.b2[root]