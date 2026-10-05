from collections import deque
class Heap:
    def __init__(self):
        self.heap_list = deque()
    def push(self, value):
        self.heap_list.append(value)
        self._heapify_up()
    def pop(self):
        if not self.heap_list:
            raise IndexError("pop from empty heap")
        root_value = self.heap_list.popleft()
        if self.heap_list:
            self.heap_list.appendleft(self.heap_list[-1])
            del self.heap_list[-1]
            self._heapify_down()
        return root_value
    def _heapify_up(self):
        current_index = len(self.heap_list) - 1
        while current_index
            self.heap_list[current_index], self.heap_list[current_index
            current_index
    def _heapify_down(self):
        current_index = 0
        while 2 * current_index + 1 < len(self.heap_list):
            left_child_index = 2 * current_index + 1
            right_child_index = left_child_index + 1 if left_child_index + 1 < len(self.heap_list) else left_child_index
            min_child_index = left_child_index if self.heap_list[left_child_index] < self.heap_list[right_child_index] else right_child_index
            if self.heap_list[current_index] <= self.heap_list[min_child_index]:
                break
            self.heap_list[current_index], self.heap_list[min_child_index] = self.heap_list[min_child_index], self.heap_list[current_index]
            current_index = min_child_index
input_list = [8, 1, 3, 4, 2, 5, 0, 9, 6, 7]
heap = Heap()
for value in input_list:
    heap.push(value)
sorted_list = []
for _ in range(len(input_list)):
    sorted_list.append(heap.pop())
print(sorted_list)