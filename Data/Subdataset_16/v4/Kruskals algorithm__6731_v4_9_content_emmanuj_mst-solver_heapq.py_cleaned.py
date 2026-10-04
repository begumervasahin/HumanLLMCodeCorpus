
from edge import Edge
class class1:
    def fonk1(self, b2):
        self.b1 = []
        self.b2 = b2
    def fonk2(self, lst):
        self.b1 = lst
        for b3 in range(self.fonk6() - 1, -1, -1):
            self.fonk8(b3)
    def fonk3(self):
        return self.b1[0] if self.b1 else None
    def fonk4(self, b3):
        if b3 = = self.fonk6() - 1:
            self.b1.pop()
        else:
            b4 = self.b1.pop()
            self.b1[b3] = b4
            if b4.weight < self.b1[b3].weight:
                self.fonk7(b3)
            else:
                self.fonk8(b3)
    def fonk5(self):
        if self.fonk6() > 0:
            self.fonk4(0)
    def fonk6(self):
        return len(self.b1)
    def fonk7(self, b3):
        while b3 > 0:
            b5 = (b3 - 1)
            if self.b1[b5].weight <= self.b1[b3].weight:
                break
            self.b1[b3], self.b1[b5] = self.b1[b5], self.b1[b3]
            b3 = b5
    def fonk8(self, b3):
        while True:
            b6 = self.fonk9(b3)
            if b6 is None or self.b1[b3].weight <= self.b1[b6].weight:
                break
            self.b1[b3], self.b1[b6] = self.b1[b6], self.b1[b3]
            b3 = b6
    def fonk9(self, b3):
        b7 = self.b2 * b3 + 1
        b8 = min(self.b2 * b3 + self.b2, self.fonk6() - 1)
        if b7 >= self.fonk6():
            return None
        b6 = b7
        for i in range(b7 + 1, b8 + 1):
            if self.b1[i].weight < self.b1[b6].weight:
                b6 = i
        return b6
    def fonk10(self):
        return str(self.b1)