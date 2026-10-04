class class1:
    def fonk1(self):
        self.b1 = [(0, 0)]
        self.a1 = 0
    def fonk2(self):
        return self.a1
    def fonk3(self):
        if self.a1 > 0:
            return self.b1[1]
        return None
    def fonk4(self):
        b2 = self.fonk3()
        if b2:
            self.b1[1] = self.b1[self.a1]
            self.a1 -= 1
            self.b1.pop()
            self.fonk8(1)
        return b2
    def fonk5(self, element):
        self.b1.append(element)
        self.a1 += 1
        self.fonk10(self.a1)
    def fonk6(self, node, new_value):
        for i in range(1, self.a1 + 1):
            if self.b1[i][1] == node:
                self.b1[i] = (new_value, node)
                self.fonk10(i)
                break
    def fonk7(self, element):
        return element in self.b1
    def fonk8(self, b4):
        while 2 * b4 <= self.a1:
            b3 = 2 * b4
            if b3 < self.a1 and self.b1[b3][0] > self.b1[b3 + 1][0]:
                b3 += 1
            if self.b1[b4][0] <= self.b1[b3][0]:
                break
            self.b1[b4], self.b1[b3] = self.b1[b3], self.b1[b4]
            b4 = b3
    def fonk9(self, elements):
        self.b1 = [(0, 0)]
        self.a1 = len(elements)
        self.b1.extend(elements)
        for i in range(len(elements)
            self.fonk8(i)
    def fonk10(self, b4):
        while b4 > 1 and self.b1[b4
            self.b1[b4
            b4
b5 = class1()
b5.fonk5((5, 'A'))
b5.fonk5((3, 'B'))
b5.fonk5((6, 'C'))
b5.fonk5((2, 'D'))
print("Minimum element:", b5.fonk3())
print("Removed b2 element:", b5.fonk4())
print("Minimum element after removal:", b5.fonk3())
b5.fonk6('C', 1)
print("Minimum element after increase_key:", b5.fonk3())