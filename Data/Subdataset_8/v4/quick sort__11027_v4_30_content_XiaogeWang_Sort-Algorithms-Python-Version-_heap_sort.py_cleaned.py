from collections import deque
class Heap:
    def __init__(self):
        self.lst = deque()
    def push(self, n):
        self.lst.append(n)
        self._up()
    def pop(self):
        res = self.lst.popleft()
        if self.lst:
            self.lst.appendleft(self.lst[-1])
            del self.lst[-1]
            self._down()
        return res
    def _up(self):
        curr = len(self.lst) - 1
        while curr
            self.lst[curr], self.lst[curr
            curr
    def _down(self):
        curr = 0
        while 2 * curr + 1 < len(self.lst):
            left = 2 * curr + 1
            right = 2 * curr + 2 if 2 * curr + 2 < len(self.lst) else left
            if self.lst[curr] <= min(self.lst[left], self.lst[right]):
                break
            if self.lst[left] < self.lst[right]:
                self.lst[curr], self.lst[left] = self.lst[left], self.lst[curr]
                curr = left
            else:
                self.lst[curr], self.lst[right] = self.lst[right], self.lst[curr]
                curr = right
a = [8, 1, 3, 4, 2, 5, 0, 9, 6, 7]
b = Heap()
for i in a:
    b.push(i)
sorted_a = []
for i in range(len(a)):
    sorted_a.append(b.pop())
print(sorted_a)