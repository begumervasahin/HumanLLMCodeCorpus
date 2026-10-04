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
    def fonk3(self):
        self.b4 = []
    def fonk4(self):
        return len(self.b4)
    def fonk5(self):
        return len(self.b4) == 0
    def fonk6(self, j):
        return (j - 1)
    def fonk7(self, j):
        return 2 * j + 1
    def fonk8(self, j):
        return 2 * j + 2
    def fonk9(self, j):
        return self.fonk7(j) < len(self.b4)
    def fonk10(self, j):
        return self.fonk8(j) < len(self.b4)
    def fonk11(self, i, j):
        self.b4[i], self.b4[j] = self.b4[j], self.b4[i]
    def fonk12(self, j):
        b5 = self.fonk6(j)
        if j > 0 and self.b4[j] < self.b4[b5]:
            self.fonk11(j, b5)
            self.fonk12(b5)
    def fonk13(self, j):
        if self.fonk9(j):
            b6 = self.fonk7(j)
            b7 = b6
            if self.fonk10(j):
                b8 = self.fonk8(j)
                if self.b4[b8] < self.b4[b6]:
                    b7 = b8
            if self.b4[b7] < self.b4[j]:
                self.fonk11(j, b7)
                self.fonk13(b7)
    def fonk14(self, key, value):
        self.b4.append(self.class3(key, value))
        self.fonk12(len(self.b4) - 1)
    def fonk15(self):
        if self.fonk5():
            raise class1('Priority queue is empty.')
        b9 = self.b4[0]
        return (b9.b2, b9.b3)
    def fonk16(self):
        if self.fonk5():
            raise class1('Priority queue is empty.')
        self.fonk11(0, len(self.b4) - 1)
        b9 = self.b4.pop()
        self.fonk13(0)
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