class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = self
        self.a1 = 0
    def fonk2(self):
        return f"class1(b1 = {self.b1}, a1={self.a1}, b2={self.b2.b1})"
class class2:
    def fonk3(self):
        self.b3 = {}
    def fonk4(self, b1):
        self.b3[b1] = class1(b1)
    def fonk5(self, b1):
        b4 = self.b3[b1].b2.b2
        while b4 != self.b3[b1].b2:
            self.b3[b1].b2 = b4
            b1 = b4.b1
            b4 = self.b3[b1].b2.b2
        return b4.b1
    def fonk6(self, u, v):
        b5 = None
        b6 = self.b3[u]
        b7 = self.b3[v]
        if b6.a1 > b7.a1:
            b7.b2 = b6
            b5 = b6
        elif b6.a1 < b7.a1:
            b6.b2 = b7
            b5 = b7
        else:
            b6.b2 = b7
            b7.a1 += 1
            b5 = b7
        return b5
    def fonk7(self):
        print(self.b3)
b8 = class2()
b8.fonk4(1)
b8.fonk4(2)
b8.fonk4(3)
print("Initial class2:")
b8.fonk7()
print("\nFinding representative of 2:", b8.fonk5(2))
print("Finding representative of 3:", b8.fonk5(3))
print("\nUnion of 2 and 3:")
b9 = b8.fonk6(2, 3)
b8.fonk7()
print("Parent of representative of 2 after union:", b9)