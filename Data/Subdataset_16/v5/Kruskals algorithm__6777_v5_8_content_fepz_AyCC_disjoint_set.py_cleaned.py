class class1:
    def fonk1(self, b1):
        self.b1 = list(b1)
        self.b2 = {element: element for element in b1}
        self.b3 = {element: 1 for element in b1}
    def fonk2(self, x):
        if self.b2[x] != x:
            self.b2[x] = self.fonk2(self.b2[x])
        return self.b2[x]
    def fonk3(self, set_a, set_b):
        b4 = self.fonk2(set_a)
        b5 = self.fonk2(set_b)
        if b4 != b5:
            if self.b3[b4] > self.b3[b5]:
                self.b2[b5] = b4
            elif self.b3[b4] < self.b3[b5]:
                self.b2[b4] = b5
            else:
                self.b2[b5] = b4
                self.b3[b4] += 1
