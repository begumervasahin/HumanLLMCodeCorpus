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
        if index > 1 and self.values[index] > self.values[index
            current_index = index
            while current_index > 1 and self.values[current_index] > self.values[current_index
                self.swap(current_index, current_index
                current_index
    def heapify_down(self, index):
        if index <= self.size
            current_index = index
            while current_index <= self.size
                child_index = 2 * current_index
                if (2 * current_index + 1) <= self.size and self.values[2 * current_index] < self.values[2 * current_index + 1]:
                    child_index = 2 * current_index + 1
                self.swap(current_index, child_index)
                current_index = child_index
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
'''
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
'''
'''
mh = MaxHeap()
mh.insert(3)
print(mh.values)
mh.insert(2)
print(mh.values)
mh.insert(1)
print(mh.values)
mh.insert(15)
print(mh.values)
mh.insert(5)
print(mh.values)
mh.insert(4)
print(mh.values)
mh.insert(45)
print(mh.values)
mh.delete(1)
print(mh.values)
print(mh.maximum())
mh.insert(677)
print(mh.values)
print(mh.maximum())
'''