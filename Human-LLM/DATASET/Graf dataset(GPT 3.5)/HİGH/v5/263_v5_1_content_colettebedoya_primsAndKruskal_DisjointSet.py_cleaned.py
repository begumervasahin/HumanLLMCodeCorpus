class class1:
    def fonk1(self, b1):
        if b1 < 0:
            raise ValueError("Size must be non-negative")
        self.b1 = b1
        self.b2 = [-1] * (b1 + 1)
    def fonk2(self, root1, root2):
        if not self.fonk4(root1) or not self.fonk4(root2):
            raise ValueError("Root value out of bounds")
        self.b2[root2] = root1
    def fonk3(self, element):
        if not self.fonk5(element):
            raise ValueError("Element value out of bounds")
        if self.b2[element] < 0:
            return element
        else:
            return self.fonk3(self.b2[element])
    def fonk4(self, root):
        return 0 <= root <= self.b1
    def fonk5(self, element):
        return 0 <= element <= self.b1