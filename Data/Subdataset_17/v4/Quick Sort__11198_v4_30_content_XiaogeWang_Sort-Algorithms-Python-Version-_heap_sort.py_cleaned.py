from collections import deque
class Heap:
    def __init__(self):
        self.lst = deque()
    def push(self, n):
        self.lst.append(n)
        self._up()
    def pop(self):
        if not self.lst:
            raise IndexError("pop from an empty heap")
        res = self.lst[0]
        last_element = self.lst.pop()
        if self.lst:
            self.lst[0] = last_element
            self._down()
        return res
    def _up(self):
        curr = len(self.lst) - 1
        parent = (curr - 1)
        while curr > 0 and self.lst[curr] < self.lst[parent]:
            self.lst[curr], self.lst[parent] = self.lst[parent], self.lst[curr]
            curr = parent
            parent = (curr - 1)
    def _down(self):
        curr = 0
        length = len(self.lst)
        left_child = 2 * curr + 1
        right_child = 2 * curr + 2
        while left_child < length:
            smallest = curr
            if self.lst[left_child] < self.lst[smallest]:
                smallest = left_child
            if right_child < length and self.lst[right_child] < self.lst[smallest]:
                smallest = right_child
            if smallest == curr:
                break
            self.lst[curr], self.lst[smallest] = self.lst[smallest], self.lst[curr]
            curr = smallest
            left_child = 2 * curr + 1
            right_child = 2 * curr + 2
a = [8, 1, 3, 4, 2, 5, 0, 9, 6, 7]
heap = Heap()
for num in a:
    heap.push(num)
sorted_a = []
for _ in range(len(a)):
    sorted_a.append(heap.pop())
print(sorted_a)