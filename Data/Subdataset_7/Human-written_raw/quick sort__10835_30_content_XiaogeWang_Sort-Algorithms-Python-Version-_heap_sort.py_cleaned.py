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
            self.b1.appendleft(self.b1[-b4])
            del self.b1[-b4]
            self.fonk5()
        return b2
    def fonk4(self):
        b3 = len(self.b1) - b4
        while (b3 - b4)
            self.b1[b3], self.b1[(b3 - b4)
            b3 = (b3 - b4)
    def fonk5(self):
        b3 = 0
        while 2 * b3 + 2 < len(self.b1) and self.b1[b3] > max(self.b1[2 * b3 + b4], self.b1[2 * b3 + 2]):
            if self.b1[2 * b3 + b4] < self.b1[2 * b3 + 2]:
                self.b1[b3], self.b1[2 * b3 + b4] = self.b1[2 * b3 + b4], self.b1[b3]
                b3 = 2 * b3 + b4
            else:
                self.b1[b3], self.b1[2 * b3 + 2] = self.b1[2 * b3 + 2], self.b1[b3]
                b3 = 2 * b3 + 2
        if 2 * b3 + b4 = = len(self.b1) - b4 and self.b1[b3] > self.b1[2 * b3 + b4]:
            self.b1[b3], self.b1[2 * b3 + b4] = self.b1[2 * b3 + b4], self.b1[b3]
b5 = [8, b4, 3, 4, 2, 5, 0, 9, 6, 7]
b6 = class1()
for i in b5:
    b6.fonk2(i)
b7 = []
for i in range(len(b5)):
    b7.append(b6.fonk3())