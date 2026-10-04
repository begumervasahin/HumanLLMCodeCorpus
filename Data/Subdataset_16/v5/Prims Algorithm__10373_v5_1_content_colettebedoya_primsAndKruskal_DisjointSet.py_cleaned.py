class class1:
    def fonk1(self, b1):
        if b1 < 0:
            raise ValueError("Size must be >= 0")
        self.b1 = b1
        self.b2 = [-1] * (b1 + 1)
    def fonk2(self, root1, root2):
        self.fonk4(root1)
        self.fonk4(root2)
        self.b2[root2] = root1
    def fonk3(self, element):
        self.fonk4(element)
        if self.b2[element] < 0:
            return element
        else:
            self.b2[element] = self.fonk3(self.b2[element])
            return self.b2[element]
    def fonk4(self, element):
        if not (0 <= element <= self.b1):
            raise ValueError(f"Element {element} is out of bounds.")