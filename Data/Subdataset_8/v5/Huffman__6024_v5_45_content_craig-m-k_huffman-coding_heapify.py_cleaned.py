class Heap:
    def __init__(self, heap_type):
        if heap_type not in ('max', 'min'):
            raise ValueError('Invalid heap type. Allowed values are "max" or "min".')
        self.queue = []
        self.heapsize = 0
        self.heap_type = heap_type
    def __len__(self):
        return len(self.queue)
    def _parent(self, i):
        return (i - 1)
    def _left_child(self, i):
        return 2 * i + 1
    def _right_child(self, i):
        return 2 * i + 2
    def _should_swap(self, parent_idx, child_idx):
        parent_value = self.queue[parent_idx]
        child_value = self.queue[child_idx]
        if self.heap_type == 'min':
            return child_value < parent_value
        else:
            return child_value > parent_value
    def _heapify_down(self, index):
        left = self._left_child(index)
        right = self._right_child(index)
        compare = min if self.heap_type == 'min' else max
        if left < self.heapsize and self._should_swap(index, left):
            smallest_or_largest = left
        else:
            smallest_or_largest = index
        if right < self.heapsize and self._should_swap(smallest_or_largest, right):
            smallest_or_largest = right
        if smallest_or_largest != index:
            self.queue[index], self.queue[smallest_or_largest] = self.queue[smallest_or_largest], self.queue[index]
            self._heapify_down(smallest_or_largest)
    def _heapify_up(self, index):
        parent = self._parent(index)
        compare = min if self.heap_type == 'min' else max
        while index > 0 and self._should_swap(parent, index):
            self.queue[index], self.queue[parent] = self.queue[parent], self.queue[index]
            index = parent
            parent = self._parent(index)
    def insert(self, key):
        self.queue.append(key)
        self.heapsize += 1
        self._heapify_up(self.heapsize - 1)
    def pop(self):
        if not self.queue:
            raise IndexError("Heap is empty")
        popped_key = self.queue[0]
        self.queue[0] = self.queue.pop()
        self.heapsize -= 1
        if self.heapsize > 0:
            self._heapify_down(0)
        return popped_key
    def build_heap(self):
        for i in range(self.heapsize
            self._heapify_down(i)