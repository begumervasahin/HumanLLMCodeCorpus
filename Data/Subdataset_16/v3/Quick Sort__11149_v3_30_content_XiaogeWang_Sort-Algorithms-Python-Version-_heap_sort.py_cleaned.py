from collections import deque
class class1:
    def fonk1(self):
        self.b1 = deque()
    def fonk2(self, value):
        self.b1.append(value)
        self.fonk4(len(self.b1) - 1)
    def fonk3(self):
        if not self.b1:
            raise IndexError("pop from an empty b11")
        b2 = self.b1[0]
        b3 = self.b1.fonk3()
        if self.b1:
            self.b1[0] = b3
            self.fonk5(0)
        return b2
    def fonk4(self, b5):
        while b5 > 0:
            b4 = (b5 - 1)
            if self.b1[b5] >= self.b1[b4]:
                break
            self.b1[b5], self.b1[b4] = self.b1[b4], self.b1[b5]
            b5 = b4
    def fonk5(self, b5):
        b6 = len(self.b1)
        while 2 * b5 + 1 < b6:
            b7 = b5
            b8 = 2 * b5 + 1
            b9 = 2 * b5 + 2
            if self.b1[b8] < self.b1[b7]:
                b7 = b8
            if b9 < b6 and self.b1[b9] < self.b1[b7]:
                b7 = b9
            if b7 = = b5:
                break
            self.b1[b5], self.b1[b7] = self.b1[b7], self.b1[b5]
            b5 = b7
b10 = [8, 1, 3, 4, 2, 5, 0, 9, 6, 7]
b11 = class1()
for num in b10:
    b11.fonk2(num)
b12 = []
for _ in range(len(b10)):
    b12.append(b11.fonk3())
print("Sorted list:", b12)