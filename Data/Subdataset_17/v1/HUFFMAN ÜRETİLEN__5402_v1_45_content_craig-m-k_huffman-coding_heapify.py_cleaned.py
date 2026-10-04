class Heap:
    def __init__(self, heap_type='max'):
        if heap_type not in {'max', 'min'}:
            raise ValueError("Heap type must be 'max' or 'min'")
        self.heap_type = heap_type
        self.queue = []
    def __len__(self):
        return len(self.queue)
    def perc_up(self, index):
        parent = (index - 1)
        while index > 0:
            if (self.heap_type == 'max' and self.queue[index] > self.queue[parent]) or \
               (self.heap_type == 'min' and self.queue[index] < self.queue[parent]):
                self.queue[index], self.queue[parent] = self.queue[parent], self.queue[index]
                index = parent
                parent = (index - 1)
            else:
                break
    def insert(self, key):
        self.queue.append(key)
        self.perc_up(len(self.queue) - 1)
    def pop(self):
        if not self.queue:
            raise IndexError("Pop from empty heap")
        root = self.queue[0]
        last_item = self.queue.pop()
        if self.queue:
            self.queue[0] = last_item
            self.heapify(0)
        return root
    def heapify(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        if self.heap_type == 'max':
            self.max_heapify(index, left, right)
        else:
            self.min_heapify(index, left, right)
    def max_heapify(self, index, left, right):
        largest = index
        if left < len(self.queue) and self.queue[left] > self.queue[largest]:
            largest = left
        if right < len(self.queue) and self.queue[right] > self.queue[largest]:
            largest = right
        if largest != index:
            self.queue[index], self.queue[largest] = self.queue[largest], self.queue[index]
            self.heapify(largest)
    def min_heapify(self, index, left, right):
        smallest = index
        if left < len(self.queue) and self.queue[left] < self.queue[smallest]:
            smallest = left
        if right < len(self.queue) and self.queue[right] < self.queue[smallest]:
            smallest = right
        if smallest != index:
            self.queue[index], self.queue[smallest] = self.queue[smallest], self.queue[index]
            self.heapify(smallest)
    def build_heap(self):
        for i in range((len(self.queue) - 2)
            self.heapify(i)
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