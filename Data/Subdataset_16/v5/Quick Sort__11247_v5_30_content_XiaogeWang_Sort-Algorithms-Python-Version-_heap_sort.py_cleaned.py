from collections import deque
class class1:
    def fonk1(self):
        self.b1 = deque()
    def fonk2(self, value):
        self.b1.append(value)
        self.fonk4()
    def fonk3(self):
        if not self.b1:
            raise IndexError("pop from an empty b1")
        b2 = self.b1[0]
        b3 = self.b1.fonk3()
        if self.b1:
            self.b1[0] = b3
            self.fonk5()
        return b2
    def fonk4(self):
        b4 = len(self.b1) - 1
        b5 = (b4 - 1)
        while b4 > 0 and self.b1[b4] < self.b1[b5]:
            self.b1[b4], self.b1[b5] = self.b1[b5], self.b1[b4]
            b4 = b5
            b5 = (b4 - 1)
    def fonk5(self):
        b4 = 0
        b6 = len(self.b1)
        b7 = 2 * b4 + 1
        b8 = 2 * b4 + 2
        while b7 < b6:
            b9 = b4
            if self.b1[b7] < self.b1[b9]:
                b9 = b7
            if b8 < b6 and self.b1[b8] < self.b1[b9]:
                b9 = b8
            if b9 = = b4:
                break
            self.b1[b4], self.b1[b9] = self.b1[b9], self.b1[b4]
            b4 = b9
            b7 = 2 * b4 + 1
            b8 = 2 * b4 + 2
b10 = [8, 1, 3, 4, 2, 5, 0, 9, 6, 7]
b1 = class1()
for num in b10:
    b1.fonk2(num)
b11 = []
for _ in range(len(b10)):
    b11.append(b1.fonk3())
print(b11)
