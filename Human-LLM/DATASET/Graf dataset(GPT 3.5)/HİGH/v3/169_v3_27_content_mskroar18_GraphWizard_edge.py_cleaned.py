class class1:
    def fonk1(self, b2, b3, b4, b1 = 0, b5=False):
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b1 = b1
        self.b5 = b5
    def fonk2(self):
        return f"class1(Vertex1: {self.b2}, Vertex2: {self.b3}, Weight: {self.b4}, Extra: {self.b1}, Selected: {self.b5})"
if b6 = = "__main__":
    b7 = class1(b2=1, b3=2, b4=5)
    b8 = class1(b2=2, b3=3, b4=7, b1=2, b5=True)
    print("class1 1:", b7)
    print("class1 2:", b8)