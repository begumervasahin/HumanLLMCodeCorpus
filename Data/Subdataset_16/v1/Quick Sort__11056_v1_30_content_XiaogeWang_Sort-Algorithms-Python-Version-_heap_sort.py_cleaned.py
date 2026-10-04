from collections import deque
class class1:
    def fonk1(self):
        self.b1 = deque()
    def fonk2(self, n):
        self.b1.append(n)
        self.fonk4()
    def fonk3(self):
        b2 = self.b1.popleft()
        if self.b1:
            self.b1.appendleft(self.b1.fonk3())
            self.fonk5()
        return b2
    def fonk4(self):
        b3 = len(self.b1) - b5
        while (b3 - b5)
            self.b1[b3], self.b1[(b3 - b5)
            b3 = (b3 - b5)
    def fonk5(self):
        b3 = 0
        while 2 * b3 + 2 < len(self.b1):
            b4 = b3
            if self.b1[2 * b3 + b5] < self.b1[b4]:
                b4 = 2 * b3 + b5
            if self.b1[2 * b3 + 2] < self.b1[b4]:
                b4 = 2 * b3 + 2
            if b4 = = b3:
                break
            self.b1[b3], self.b1[b4] = self.b1[b4], self.b1[b3]
            b3 = b4
        if 2 * b3 + b5 = = len(self.b1) - b5 and self.b1[b3] > self.b1[2 * b3 + b5]:
            self.b1[b3], self.b1[2 * b3 + b5] = self.b1[2 * b3 + b5], self.b1[b3]
b6 = [8, b5, 3, 4, 2, 5, 0, 9, 6, 7]
b7 = class1()
for i in b6:
    b7.fonk2(i)
b8 = []
for i in range(len(b6)):
    b8.append(b7.fonk3())
print("Sorted list:", b8)