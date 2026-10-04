class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = self
        self.a1 = 0
class class2:
    def fonk2(self):
        self.b3 = {}
    def fonk3(self, b1):
        self.b3[b1] = class1(b1)
    def fonk4(self, b1):
        b4 = self.b3[b1]
        if b4.b2 != b4:
            b4.b2 = self.b3[self.fonk4(b4.b2.b1)]
        return b4.b2.b1
    def fonk5(self, value1, value2):
        b5 = self.b3[self.fonk4(value1)]
        b6 = self.b3[self.fonk4(value2)]
        if b5.b1 != b6.b1:
            if b5.a1 > b6.a1:
                b6.b2 = b5
                return b5
            elif b5.a1 < b6.a1:
                b5.b2 = b6
                return b6
            else:
                b6.b2 = b5
                b5.a1 += 1
                return b5
    def fonk6(self):
        print("Disjoint Set Structure:")
        for b1, b4 in self.b3.items():
            print(f"class1: {b1}, Parent: {b4.b2.b1}, Rank: {b4.a1}")
if b7 = = "__main__":
    b8 = class2()
    b9 = [1, 2, 3, 4]
    for element in b9:
        b8.fonk3(element)
    print("Initial sets:")
    b8.fonk6()
    b8.fonk5(1, 2)
    b8.fonk5(3, 4)
    b8.fonk5(2, 3)
    print("\nAfter some unions:")
    b8.fonk6()
    print("\nFind representative of element 4:", b8.fonk4(4))