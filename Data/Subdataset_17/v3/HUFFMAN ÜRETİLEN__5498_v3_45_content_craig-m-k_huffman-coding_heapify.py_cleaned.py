class Heap:
    def __init__(self, heap_type='max'):
        self._validate_heap_type(heap_type)
        self.heap_type = heap_type
        self.queue = []
    def __len__(self):
        return len(self.queue)
    def insert(self, key):
        self.queue.append(key)
        self._percolate_up(len(self.queue) - 1)
    def pop(self):
        if not self.queue:
            raise IndexError("Pop from empty heap")
        root = self.queue[0]
        last_item = self.queue.pop()
        if self.queue:
            self.queue[0] = last_item
            self._heapify_down(0)
        return root
    def build_heap(self, elements):
        self.queue = elements[:]
        start_index = (len(self.queue) - 2)
        for i in range(start_index, -1, -1):
            self._heapify_down(i)
    def _percolate_up(self, index):
        while index > 0:
            parent = (index - 1)
            if self._should_swap(self.queue[index], self.queue[parent]):
                self._swap(index, parent)
                index = parent
            else:
                break
    def _heapify_down(self, index):
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest_or_smallest = index
            if left < len(self.queue) and self._should_swap(self.queue[left], self.queue[largest_or_smallest]):
                largest_or_smallest = left
            if right < len(self.queue) and self._should_swap(self.queue[right], self.queue[largest_or_smallest]):
                largest_or_smallest = right
            if largest_or_smallest != index:
                self._swap(index, largest_or_smallest)
                index = largest_or_smallest
            else:
                break
    def _should_swap(self, child, parent):
        if self.heap_type == 'max':
            return child > parent
        return child < parent
    def _swap(self, i, j):
        self.queue[i], self.queue[j] = self.queue[j], self.queue[i]
    def _validate_heap_type(self, heap_type):
        if heap_type not in {'max', 'min'}:
            raise ValueError("Heap type must be 'max' or 'min'")
if __name__ == "__main__":
    max_heap = Heap('max')
    max_heap.insert(10)
    max_heap.insert(20)
    max_heap.insert(5)
    max_heap.insert(15)
    print("Max Heap:", max_heap.queue)
    print("Popped from Max Heap:", max_heap.pop())
    print("Max Heap after pop:", max_heap.queue)
    min_heap = Heap('min')
    min_heap.insert(10)
    min_heap.insert(20)
    min_heap.insert(5)
    min_heap.insert(15)
    print("Min Heap:", min_heap.queue)
    print("Popped from Min Heap:", min_heap.pop())
    print("Min Heap after pop:", min_heap.queue)