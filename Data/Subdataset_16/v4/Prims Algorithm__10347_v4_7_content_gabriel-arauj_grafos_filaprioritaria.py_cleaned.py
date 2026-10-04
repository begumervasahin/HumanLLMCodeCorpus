class class1:
    def fonk1(self):
        self.b1 = [(0, 0)]
        self.a1 = 0
    def fonk2(self):
        return self.a1
    def fonk3(self):
        if self.a1 != 0:
            return self.b1[1]
    def fonk4(self):
        b2 = self.fonk3()
        self.b1[1] = self.b1[self.a1]
        self.a1 -= 1
        self.b1.pop()
        self.fonk8(1)
        return b2
    def fonk5(self, element):
        self.b1.append(element)
        self.a1 += 1
        self.fonk10(self.a1)
    def fonk6(self, node, value):
        for b4 in range(1, self.a1 + 1):
            if self.b1[b4][1] == node:
                self.b1[b4] = (value, node)
                self.fonk10(b4)
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
        self.b1 = [(0, 0)] + elements
        self.a1 = len(elements)
        for b4 in range(self.a1
            self.fonk8(b4)
    def fonk10(self, b4):
        while b4 > 1 and self.b1[b4][0] < self.b1[b4
            self.b1[b4], self.b1[b4
            b4