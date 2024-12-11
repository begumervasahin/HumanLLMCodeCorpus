class class1:
    b1 = 'b2', 'b3'
    def fonk1(self, b2, next_node):
        self.b2 = b2
        self.b3 = next_node
    def fonk2(self, other):
        return self.b2 <= other.b2
    def fonk3(self, other):
        return self.b2 <= other.b2
class class2:
    def fonk4(self):
        self.b4 = None
        self.b5 = None
        self.a1 = 0
    def fonk5(self):
        b4 = self.b4
        b6 = []
        while b4:
            b6.append(str(b4.b2))
            b4 = b4.b3
        return ", ".join(b6)
    b7 = __str__
    def fonk6(self):
        return self.a1
    def fonk7(self):
        return self.a1 = = 0
    def fonk8(self):
        if self.fonk7():
            raise IndexError("Queue is empty")
        b8 = self.b4.b2
        self.b4 = self.b4.b3
        self.a1 -= 1
        if self.fonk7():
            self.b5 = None
        return b8
    def fonk9(self, element):
        b9 = class1(element, None)
        if self.fonk7():
            self.b4 = b9
        else:
            self.b5.b3 = b9
        self.b5 = b9
        self.a1 += 1
    def fonk10(self, index):
        if not (0 <= index < self.a1):
            raise IndexError("Index out of range")
        b10 = self.b4
        for _ in range(index):
            b10 = b10.b3
        return b10.b2
    def fonk11(self, index, b2):
        if not (0 <= index < self.a1):
            raise IndexError("Index out of range")
        b10 = self.b4
        for _ in range(index):
            b10 = b10.b3
        b10.b2 = b2
if b11 = = "__main__":
    b12 = class2()
    b12.fonk9(1)
    b12.fonk9(2)
    b12.fonk9(3)
    print("Queue:", b12)
    print("Length:", len(b12))
    print("Dequeue:", b12.fonk8())
    print("Queue after dequeue:", b12)
    b12[0] = 5
    print("Queue after setting value at index 0:", b12)