class class1(Exception):
    pass
class class2:
    class class3:
        b1 = 'b2', 'b3'
        def fonk1(self, k, v):
            self.b2 = k
            self.b3 = v
        def fonk2(self, other):
            return self.b2 < other.b2
class class4(class2):
    def fonk3(self, j):
        return (j - 1)
    def fonk4(self, j):
        return 2 * j + 1
    def fonk5(self, j):
        return 2 * j + 2
    def fonk6(self, j):
        return self.fonk4(j) < len(self.b8)
    def fonk7(self, j):
        return self.fonk5(j) < len(self.b8)
    def fonk8(self, i, j):
        self.b8[i], self.b8[j] = self.b8[j], self.b8[i]
    def fonk9(self, j):
        b4 = self.fonk3(j)
        if j > 0 and self.b8[j] < self.b8[b4]:
            self.fonk8(j, b4)
            self.fonk9(b4)
    def fonk10(self, j):
        if self.fonk6(j):
            b5 = self.fonk4(j)
            b6 = b5
            if self.fonk7(j):
                b7 = self.fonk5(j)
                if self.b8[b7] < self.b8[b5]:
                    b6 = b7
            if self.b8[b6] < self.b8[j]:
                self.fonk8(j, b6)
                self.fonk10(b6)
    def fonk11(self):
        self.b8 = []
    def fonk12(self):
        return len(self.b8)
    def fonk13(self):
        return len(self.b8) == 0
    def fonk14(self, key, value):
        self.b8.append(self.class3(key, value))
        self.fonk9(len(self.b8) - 1)
    def fonk15(self):
        if self.fonk13():
            raise class1('Priority queue is empty.')
        b9 = self.b8[0]
        return (b9.b2, b9.b3)
    def fonk16(self):
        if self.fonk13():
            raise class1('Priority queue is empty.')
        self.fonk8(0, len(self.b8) - 1)
        b9 = self.b8.pop()
        self.fonk10(0)
        return (b9.b2, b9.b3)
if b10 = = "__main__":
    b11 = class4()
    b11.fonk14(5, 'A')
    b11.fonk14(9, 'C')
    b11.fonk14(3, 'B')
    b11.fonk14(7, 'D')
    print("Min element:", b11.fonk15())
    print("Remove min element:", b11.fonk16())
    print("Min element:", b11.fonk15())
    print("Remove min element:", b11.fonk16())
    print("Min element:", b11.fonk15())