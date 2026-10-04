from collections import deque
class Heap:
    def __init__(self):
        self.lst = deque()
    def push(self, n):
        self.lst.append(n)
        self._sift_up(len(self.lst) - 1)
    def pop(self):
        if not self.lst:
            raise IndexError("pop from an empty heap")
        top_element = self.lst[0]
        last_element = self.lst.pop()
        if self.lst:
            self.lst[0] = last_element
            self._sift_down(0)
        return top_element
    def _sift_up(self, idx):
        while idx > 0:
            parent_idx = (idx - 1)
            if self.lst[idx] >= self.lst[parent_idx]:
                break
            self.lst[idx], self.lst[parent_idx] = self.lst[parent_idx], self.lst[idx]
            idx = parent_idx
    def _sift_down(self, idx):
        length = len(self.lst)
        while 2 * idx + 1 < length:
            smallest = idx
            left_child = 2 * idx + 1
            right_child = 2 * idx + 2
            if self.lst[left_child] < self.lst[smallest]:
                smallest = left_child
            if right_child < length and self.lst[right_child] < self.lst[smallest]:
                smallest = right_child
            if smallest == idx:
                break
            self.lst[idx], self.lst[smallest] = self.lst[smallest], self.lst[idx]
            idx = smallest
a = [8, 1, 3, 4, 2, 5, 0, 9, 6, 7]
heap = Heap()
for num in a:
    heap.push(num)
sorted_a = []
for _ in range(len(a)):
    sorted_a.append(heap.pop())
print("Sorted list:", sorted_a)