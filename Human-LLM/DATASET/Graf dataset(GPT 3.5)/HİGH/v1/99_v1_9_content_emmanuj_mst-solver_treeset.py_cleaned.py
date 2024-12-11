class class1:
    def fonk1(self, val):
        self.b1 = val
        self.b2 = self
        self.a1 = 0
    def fonk2(self):
        return "b5 " + str(self.b1) + " r " + str(self.a1) + " p " + str(self.b2.b1)
class class2:
    def fonk3(self):
        self.b3 = {}
    def fonk4(self, b5):
        self.b3[b5] = class1(b5)
    def fonk5(self, b5):
        b4 = self.b3[b5].b2.b2
        while b4 != self.b3[b5].b2:
            self.b3[b5].b2 = b4
            b5 = b4.b1
            b4 = self.b3[b5].b2.b2
        return b4.b1
    def fonk6(self, u, v):
        b6 = None
        if self.b3[u].a1 > self.b3[v].a1:
            self.b3[v].b2 = self.b3[u]
            b6 = self.b3[u]
        elif self.b3[u].a1 < self.b3[v].a1:
            self.b3[u].b2 = self.b3[v]
            b6 = self.b3[v]
        else:
            self.b3[u].b2 = self.b3[v]
            self.b3[v].a1 = self.b3[v].a1 + 1
            b6 = self.b3[v]
        return b6
    def fonk7(self):
        print(self.b3)
b7 = class2()
b7.fonk4(1)
b7.fonk4(2)
b7.fonk4(3)
print("Initial class2:")
b7.fonk7()
print("\nFinding representative of 2:", b7.fonk5(2))
print("Finding representative of 3:", b7.fonk5(3))
print("\nUnion of 2 and 3:")
b6 = b7.fonk6(2, 3)
b7.fonk7()
print("Parent of representative of 2 after union:", b6)