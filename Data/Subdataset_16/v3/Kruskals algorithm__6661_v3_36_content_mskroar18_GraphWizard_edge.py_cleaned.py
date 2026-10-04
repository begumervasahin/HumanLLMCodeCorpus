class class1:
    def fonk1(self, b2, b3, b4, b1 = 0, b5=False):
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b1 = b1
        self.b5 = b5
    def fonk2(self):
        return (
            f"class1(Vertex 1: {self.b2}, "
            f"Vertex 2: {self.b3}, "
            f"Weight: {self.b4}, "
            f"Selected: {self.b5})"
        )
if b6 = = "__main__":
    b7 = class1(1, 2, 10, b5=True)
    print(b7)