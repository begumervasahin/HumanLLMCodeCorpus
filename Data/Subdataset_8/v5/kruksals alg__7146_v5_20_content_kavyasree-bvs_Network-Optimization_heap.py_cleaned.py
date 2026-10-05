class MaxHeap:
    def __init__(self):
        self.heap = [-1]
        self.values = [-1]
        self.size = 0
    def maximum(self):
        return self.heap[1]
    def insert(self, name, value):
        self.size += 1
        self.heap.append(name)
        self.values.append(value)
        self.heapify_up(self.size)
    def update(self, name, value):
        print(value)
        print(self.size)
    def delete(self, index):
        if self.size == 1 or index == self.size:
            self.values.pop()
            self.heap.pop()
            self.size -= 1
        else:
            self.values[index] = self.values.pop()
            self.heap[index] = self.heap.pop()
            self.size -= 1
            self.heapify_down(index)
    def heapify_up(self, index):
        while index > 1 and self.values[index] > self.values[index
            self.swap(index, index
            index
    def heapify_down(self, index):
        while index <= self.size
            child_index = self.find_max_child_index(index)
            if self.values[index] < self.values[child_index]:
                self.swap(index, child_index)
                index = child_index
            else:
                break
    def find_max_child_index(self, index):
        left_child_index = 2 * index
        right_child_index = 2 * index + 1 if 2 * index + 1 <= self.size else None
        if right_child_index and self.values[left_child_index] < self.values[right_child_index]:
            return right_child_index
        else:
            return left_child_index
    def swap(self, index1, index2):
        self.values[index1], self.values[index2] = self.values[index2], self.values[index1]
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
    def heap_sort(self):
        sorted_edges = []
        sorted_weights = []
        while self.size >= 1:
            sorted_edges.append(self.heap[1])
            sorted_weights.append(self.values[1])
            self.delete(1)
        return [sorted_weights, sorted_edges]
mh = MaxHeap()
mh.insert(1, 10)
print('\n', mh.heap, mh.values)
mh.insert(2, 30)
print('\n', mh.heap, mh.values)
mh.insert(3, 40)
print('\n', mh.heap, mh.values)
mh.insert(4, 15)
print('\n', mh.heap, mh.values)
mh.insert(5, 60)
print('\n', mh.heap, mh.values)
print(mh.maximum())
mh.delete(1)
print('\n', mh.heap, mh.values)
print(mh.maximum())