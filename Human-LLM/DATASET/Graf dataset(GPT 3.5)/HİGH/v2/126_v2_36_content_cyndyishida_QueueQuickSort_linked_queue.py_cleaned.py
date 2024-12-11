class class1:
    def fonk1(self, b1, next_node):
        self.b1 = b1
        self.b2 = next_node
    def fonk2(self, other):
        return self.b1 <= other.b1
    def fonk3(self, other):
        return self.b1 <= other.b1
class class2:
    def fonk4(self):
        self.b3 = None
        self.b4 = None
        self.a1 = 0
    def fonk5(self):
        b5 = self.b3
        b6 = []
        while b5:
            b6.append(str(b5.b1))
            b5 = b5.b2
        return ", ".join(b6)
    b7 = __str__
    def fonk6(self):
        return self.a1
    def fonk7(self):
        return self.a1 = = 0
    def fonk8(self):
        if self.fonk7():
            raise IndexError("Queue is empty")
        b1 = self.b3.b1
        self.b3 = self.b3.b2
        self.a1 -= 1
        if self.fonk7():
            self.b4 = None
        return b1
    def fonk9(self, element):
        b8 = class1(element, None)
        if self.fonk7():
            self.b3 = b8
        else:
            self.b4.b2 = b8
        self.b4 = b8
        self.a1 += 1
    def fonk10(self, index):
        if not (0 <= index < self.a1):
            raise IndexError("Index out of range")
        b5 = self.b3
        for _ in range(index):
            b5 = b5.b2
        return b5.b1
    def fonk11(self, index, b1):
        if not (0 <= index < self.a1):
            raise IndexError("Index out of range")
        b5 = self.b3
        for _ in range(index):
            b5 = b5.b2
        b5.b1 = b1
if b9 = = "__main__":
    b10 = class2()
    b10.fonk9(1)
    b10.fonk9(2)
    b10.fonk9(3)
    print("Queue:", b10)
    print("Length:", len(b10))
    print("Dequeue:", b10.fonk8())
    print("Queue after dequeue:", b10)
    b10[0] = 5
    print("Queue after setting b1 at index 0:", b10)