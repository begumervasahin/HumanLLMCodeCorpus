class class1:
    def fonk1(self, b2, b1 = None):
        self.b2 = b2
        self.b1 = b1
    def fonk2(self):
        return str(self.b2)
class class2:
    def fonk3(self):
        self.b3 = None
        self.b4 = None
        self.a1 = 0
    def fonk4(self, b2):
        b5 = class1(b2)
        if self.b3 is None:
            self.b3 = b5
        else:
            self.b4.b1 = b5
        self.b4 = b5
        self.a1 += 1
    def fonk5(self, index):
        if index >= self.a1 or index < 0:
            raise IndexError('Index out of bounds')
        b6 = self.b3
        for _ in range(index):
            b6 = b6.b1
        return b6.b2
    def fonk6(self):
        return self.a1
    def fonk7(self):
        b6 = self.b3
        while b6:
            yield b6.b2
            b6 = b6.b1
    def fonk8(self):
        b7 = [str(node) for node in self]
        return " -> ".join(b7)
if b8 = = "__main__":
    b9 = class2()
    b9.fonk4(1)
    b9.fonk4(5)
    b9.fonk4(-7)
    print(f"Linked list b7: {b9}")
    print(f"Size of linked list: {len(b9)}")
    print(f"Element at index 1: {b9.fonk5(1)}")