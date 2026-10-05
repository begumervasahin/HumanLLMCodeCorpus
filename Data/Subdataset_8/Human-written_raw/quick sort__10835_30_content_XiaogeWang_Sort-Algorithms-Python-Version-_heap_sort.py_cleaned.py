from collections import deque
class Heap:
    def __init__(self):
        self.lst = deque()
    def push(self, n):
        self.lst.append(n)
        self.up()
    def pop(self):
        res = self.lst.popleft()
        if self.lst:
            self.lst.appendleft(self.lst[-1])
            del self.lst[-1]
            self.down()
        return res
    def up(self):
        curr = len(self.lst) - 1
        while (curr - 1)
            self.lst[curr], self.lst[(curr - 1)
            curr = (curr - 1)
    def down(self):
        curr = 0
        while 2 * curr + 2 < len(self.lst) and self.lst[curr] > max(self.lst[2 * curr + 1], self.lst[2 * curr + 2]):
            if self.lst[2 * curr + 1] < self.lst[2 * curr + 2]:
                self.lst[curr], self.lst[2 * curr + 1] = self.lst[2 * curr + 1], self.lst[curr]
                curr = 2 * curr + 1
            else:
                self.lst[curr], self.lst[2 * curr + 2] = self.lst[2 * curr + 2], self.lst[curr]
                curr = 2 * curr + 2
        if 2 * curr + 1 == len(self.lst) - 1 and self.lst[curr] > self.lst[2 * curr + 1]:
            self.lst[curr], self.lst[2 * curr + 1] = self.lst[2 * curr + 1], self.lst[curr]
a = [8, 1, 3, 4, 2, 5, 0, 9, 6, 7]
b = Heap()
for i in a:
    b.push(i)
sorted_a = []
for i in range(len(a)):
    sorted_a.append(b.pop())