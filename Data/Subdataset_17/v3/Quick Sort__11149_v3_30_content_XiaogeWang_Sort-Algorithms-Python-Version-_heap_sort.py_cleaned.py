from collections import deque
class Heap:
    def __init__(self):
        self.data = deque()
    def push(self, value):
        self.data.append(value)
        self._sift_up(len(self.data) - 1)
    def pop(self):
        if not self.data:
            raise IndexError("pop from an empty heap")
        top_value = self.data[0]
        last_value = self.data.pop()
        if self.data:
            self.data[0] = last_value
            self._sift_down(0)
        return top_value
    def _sift_up(self, idx):
        while idx > 0:
            parent_idx = (idx - 1)
            if self.data[idx] >= self.data[parent_idx]:
                break
            self.data[idx], self.data[parent_idx] = self.data[parent_idx], self.data[idx]
            idx = parent_idx
    def _sift_down(self, idx):
        length = len(self.data)
        while 2 * idx + 1 < length:
            smallest = idx
            left_child = 2 * idx + 1
            right_child = 2 * idx + 2
            if self.data[left_child] < self.data[smallest]:
                smallest = left_child
            if right_child < length and self.data[right_child] < self.data[smallest]:
                smallest = right_child
            if smallest == idx:
                break
            self.data[idx], self.data[smallest] = self.data[smallest], self.data[idx]
            idx = smallest
test_data = [8, 1, 3, 4, 2, 5, 0, 9, 6, 7]
heap = Heap()
for num in test_data:
    heap.push(num)
sorted_data = []
for _ in range(len(test_data)):
    sorted_data.append(heap.pop())
print("Sorted list:", sorted_data)