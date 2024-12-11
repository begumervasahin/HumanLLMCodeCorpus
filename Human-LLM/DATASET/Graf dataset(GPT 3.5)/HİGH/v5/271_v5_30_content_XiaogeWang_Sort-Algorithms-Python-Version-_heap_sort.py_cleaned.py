from collections import deque
class class1:
    def fonk1(self):
        self.b1 = deque()
    def fonk2(self, value):
        self.b1.append(value)
        self.fonk4()
    def fonk3(self):
        if not self.b1:
            raise IndexError("pop from empty b8")
        b2 = self.b1.popleft()
        if self.b1:
            self.b1.appendleft(self.b1[-1])
            del self.b1[-1]
            self.fonk5()
        return b2
    def fonk4(self):
        b3 = len(self.b1) - 1
        while b3
            self.b1[b3], self.b1[b3
            b3
    def fonk5(self):
        b3 = 0
        while 2 * b3 + 1 < len(self.b1):
            b4 = 2 * b3 + 1
            b5 = b4 + 1 if b4 + 1 < len(self.b1) else b4
            b6 = b4 if self.b1[b4] < self.b1[b5] else b5
            if self.b1[b3] <= self.b1[b6]:
                break
            self.b1[b3], self.b1[b6] = self.b1[b6], self.b1[b3]
            b3 = b6
b7 = [8, 1, 3, 4, 2, 5, 0, 9, 6, 7]
b8 = class1()
for value in b7:
    b8.fonk2(value)
b9 = []
for _ in range(len(b7)):
    b9.append(b8.fonk3())
print(b9)