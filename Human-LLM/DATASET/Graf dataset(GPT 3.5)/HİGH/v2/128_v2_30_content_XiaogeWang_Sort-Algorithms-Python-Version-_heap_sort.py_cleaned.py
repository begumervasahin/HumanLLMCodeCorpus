from collections import deque
class class1:
    def fonk1(self):
        self.b1 = deque()
    def fonk2(self, value):
        self.b1.append(value)
        self.fonk4()
    def fonk3(self):
        if not self.b1:
            raise IndexError("Heap is empty")
        b2 = self.b1[0]
        if len(self.b1) > 1:
            self.b1[0] = self.b1.fonk3()
            self.fonk5()
        else:
            self.b1.fonk3()
        return b2
    def fonk4(self):
        b3 = len(self.b1) - 1
        while b3 > 0 and self.b1[b3] < self.b1[(b3 - 1)
            self.b1[b3], self.b1[(b3 - 1)
            b3 = (b3 - 1)
    def fonk5(self):
        b3 = 0
        while (2 * b3 + 1) < len(self.b1):
            b4 = 2 * b3 + 1
            if (b4 + 1) < len(self.b1) and self.b1[b4 + 1] < self.b1[b4]:
                b4 += 1
            if self.b1[b3] <= self.b1[b4]:
                break
            self.b1[b3], self.b1[b4] = self.b1[b4], self.b1[b3]
            b3 = b4
b5 = [8, 1, 3, 4, 2, 5, 0, 9, 6, 7]
b1 = class1()
for value in b5:
    b1.fonk2(value)
b6 = []
for _ in range(len(b5)):
    b6.append(b1.fonk3())
print(b6)