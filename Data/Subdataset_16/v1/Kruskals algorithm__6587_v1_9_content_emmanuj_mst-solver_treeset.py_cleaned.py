class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = self
        self.a1 = 0
class class2:
    def fonk2(self):
        self.b3 = {}
    def fonk3(self, n):
        self.b3[n] = class1(n)
    def fonk4(self, n):
        if self.b3[n].b2 != self.b3[n]:
            self.b3[n].b2 = self.b3[self.fonk4(self.b3[n].b2.b1)]
        return self.b3[n].b2.b1
    def fonk5(self, u, v):
        b4 = self.b3[self.fonk4(u)]
        b5 = self.b3[self.fonk4(v)]
        if b4.b1 != b5.b1:
            if b4.a1 > b5.a1:
                b5.b2 = b4
                return b4
            elif b4.a1 < b5.a1:
                b4.b2 = b5
                return b5
            else:
                b5.b2 = b4
                b4.a1 += 1
                return b4
    def fonk6(self):
        for key in self.b3:
            b6 = self.b3[key]
            print(f"class1: {key}, Parent: {b6.b2.b1}, Rank: {b6.a1}")
if b7 = = "__main__":
    b8 = class2()
    b8.fonk3(1)
    b8.fonk3(2)
    b8.fonk3(3)
    b8.fonk3(4)
    print("Initial sets:")
    b8.fonk6()
    b8.fonk5(1, 2)
    b8.fonk5(3, 4)
    b8.fonk5(2, 3)
    print("\nAfter some unions:")
    b8.fonk6()
    print("\nFind representative of element 4:", b8.fonk4(4))