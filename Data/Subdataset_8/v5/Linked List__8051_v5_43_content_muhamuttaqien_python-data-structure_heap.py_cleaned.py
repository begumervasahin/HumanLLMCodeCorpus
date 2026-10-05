class MaxHeap:
    def __init__(self):
        self.heap = []
        self.size = 0
    def left_child_index(self, i):
        left_index = 2 * i + 1
        return left_index if left_index < self.size else None
    def right_child_index(self, i):
        right_index = 2 * i + 2
        return right_index if right_index < self.size else None
    def max_heapify(self, i):
        largest = i
        left_index = self.left_child_index(i)
        right_index = self.right_child_index(i)
        if left_index is not None and self.heap[left_index] > self.heap[largest]:
            largest = left_index
        if right_index is not None and self.heap[right_index] > self.heap[largest]:
            largest = right_index
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest)
    def build_heap(self, array):
        self.heap = list(array)
        self.size = len(array)
        for i in range(self.size
            self.max_heapify(i)
    def heap_sort(self):
        for i in range(self.size - 1, 0, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self.size -= 1
            self.max_heapify(0)
        self.size = len(self.heap)
    def insert(self, data):
        self.heap.append(data)
        self.size += 1
        curr = self.size - 1
        while curr > 0 and self.heap[curr] > self.heap[curr
            self.heap[curr], self.heap[curr
            curr
    def display(self):
        print(self.heap)
def main():
    print("=== Max Heap ===")
    sentence = input("[STR] Enter your sentence: ").split()
    heap = MaxHeap()
    heap.build_heap(sentence)
    heap.heap_sort()
    heap.display()
if __name__ == '__main__':
    main()