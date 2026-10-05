class Heap:
    def __init__(self, heap_type):
        if heap_type not in ('max', 'min'):
            raise ValueError('Invalid heap type. Use "max" or "min".')
        self.heap_type = heap_type
        self.queue = []
        self.heapsize = 0
    def __len__(self):
        return len(self.queue)
    def perc_up(self, index):
        parent_index = (index + 1)
        while index > 0 and ((self.heap_type == 'max' and self.queue[parent_index] < self.queue[index]) or
                             (self.heap_type == 'min' and self.queue[parent_index] > self.queue[index])):
            self.queue[index], self.queue[parent_index] = self.queue[parent_index], self.queue[index]
            index = parent_index
            parent_index = (index + 1)
    def insert(self, key):
        self.queue.append(key)
        self.heapsize += 1
        self.perc_up(self.heapsize - 1)
    def pop(self):
        last_index = self.heapsize - 1
        self.queue[last_index], self.queue[0] = self.queue[0], self.queue[last_index]
        popped_key = self.queue.pop()
        self.heapsize -= 1
        self.heapify(0)
        return popped_key
    def heapify(self, index):
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        n = self.heapsize
        if self.heap_type == 'max':
            largest_index = index
            if left_index < n and self.queue[left_index] > self.queue[largest_index]:
                largest_index = left_index
            if right_index < n and self.queue[right_index] > self.queue[largest_index]:
                largest_index = right_index
            if largest_index != index:
                self.queue[index], self.queue[largest_index] = self.queue[largest_index], self.queue[index]
                self.heapify(largest_index)
        else:
            smallest_index = index
            if left_index < n and self.queue[left_index] < self.queue[smallest_index]:
                smallest_index = left_index
            if right_index < n and self.queue[right_index] < self.queue[smallest_index]:
                smallest_index = right_index
            if smallest_index != index:
                self.queue[index], self.queue[smallest_index] = self.queue[smallest_index], self.queue[index]
                self.heapify(smallest_index)
    def build_heap(self):
        n = self.heapsize
        for i in range(n
            self.heapify(i)
max_heap = Heap('max')
max_heap.insert(4)
max_heap.insert(1)
max_heap.insert(7)
max_heap.insert(3)
print("Max Heap:", max_heap.queue)
min_heap = Heap('min')
min_heap.insert(4)
min_heap.insert(1)
min_heap.insert(7)
min_heap.insert(3)
print("Min Heap:", min_heap.queue)