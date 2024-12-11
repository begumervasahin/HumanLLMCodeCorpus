class class1:
    def fonk1(self, b2, b1 = None):
        self.b2 = b2
        self.b3 = b1
class class2:
    def fonk2(self):
        self.b4 = None
        self.b5 = None
        self.a1 = 0
    def fonk3(self):
        b6 = [str(node.b2) for node in self]
        return ", ".join(b6)
    b7 = __str__
    def fonk4(self):
        return self.a1
    def fonk5(self):
        b8 = self.b4
        while b8:
            yield b8
            b8 = b8.b3
    def fonk6(self):
        return self.a1 = = 0
    def fonk7(self):
        if self.fonk6():
            raise IndexError("Queue is empty")
        b2 = self.b4.b2
        self.b4 = self.b4.b3
        self.a1 -= 1
        if self.fonk6():
            self.b5 = None
        return b2
    def fonk8(self, element):
        b9 = class1(element)
        if self.fonk6():
            self.b4 = b9
        else:
            self.b5.b3 = b9
        self.b5 = b9
        self.a1 += 1
    def fonk9(self, index):
        if not (0 <= index < self.a1):
            raise IndexError("Index out of range")
        b8 = self.b4
        for _ in range(index):
            b8 = b8.b3
        return b8.b2
    def fonk10(self, index, b2):
        if not (0 <= index < self.a1):
            raise IndexError("Index out of range")
        b8 = self.b4
        for _ in range(index):
            b8 = b8.b3
        b8.b2 = b2
if b10 = = "__main__":
    b11 = class2()
    b11.fonk8(1)
    b11.fonk8(2)
    b11.fonk8(3)
    print("Queue:", b11)
    print("Length:", len(b11))
    print("Dequeue:", b11.fonk7())
    print("Queue after dequeue:", b11)
    b11[0] = 5
    print("Queue after setting b2 at index 0:", b11)