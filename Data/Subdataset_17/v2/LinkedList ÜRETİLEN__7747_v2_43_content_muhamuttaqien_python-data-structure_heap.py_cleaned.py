class MaxHeap:
    def __init__(self):
        self.heap = []
        self.size = 0
    def _left_child(self, index):
        left_index = 2 * index + 1
        return left_index if left_index < self.size else None
    def _right_child(self, index):
        right_index = 2 * index + 2
        return right_index if right_index < self.size else None
    def _max_heapify(self, index):
        largest = index
        left = self._left_child(index)
        right = self._right_child(index)
        if left is not None and self.heap[left] > self.heap[largest]:
            largest = left
        if right is not None and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._max_heapify(largest)
    def build_heap(self, array):
        self.size = len(array)
        self.heap = array[:]
        for i in range(self.size
            self._max_heapify(i)
    def extract_max(self):
        if self.size == 0:
            return None
        max_elem = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self._max_heapify(0)
        return max_elem
    def heap_sort(self):
        original_size = self.size
        for i in range(self.size - 1, 0, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self.size -= 1
            self._max_heapify(0)
        self.size = original_size
    def insert(self, data):
        self.heap.append(data)
        self.size += 1
        current = self.size - 1
        while current > 0 and self.heap[current] > self.heap[(current - 1)
            self.heap[current], self.heap[(current - 1)
            current = (current - 1)
    def display(self):
        print(self.heap)
def main():
    print("=== MaxHeap ===")
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    heap = MaxHeap()
    heap.build_heap(words)
    heap.heap_sort()
    heap.display()
if __name__ == '__main__':
    main()