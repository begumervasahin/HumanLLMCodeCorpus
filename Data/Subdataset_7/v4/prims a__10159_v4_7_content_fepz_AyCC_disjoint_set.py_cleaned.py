class class1:
    def fonk1(self, b1):
        self.b1 = list(b1)
        self.b2 = list(range(len(b1)))
        self.b3 = [1] * len(b1)
    def fonk2(self, element):
        b4 = b5 = self.b1.b4(element)
        while self.b2[b5] != b5:
            b5 = self.b2[b5]
        while b4 != b5:
            b6 = self.b2[b4]
            self.b2[b4] = b5
            b4 = b6
        return b5
    def fonk3(self, set_a, set_b):
        if self.b3[set_a] == self.b3[set_b]:
            self.b3[set_a] += 1
            self.b2[set_b] = set_a
        else:
            if self.b3[set_a] > self.b3[set_b]:
                self.b2[set_b] = set_a
            else:
                self.b2[set_a] = set_b