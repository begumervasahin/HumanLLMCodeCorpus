class Heap:
    def __init__(self):
        self.h = []
        self.currsize = 0
    def _left_child(self, i):
        left = 2 * i + 1
        return left if left < self.currsize else None
    def _right_child(self, i):
        right = 2 * i + 2
        return right if right < self.currsize else None
    def _max_heapify(self, i):
        largest = i
        left = self._left_child(i)
        right = self._right_child(i)
        if left is not None and self.h[left] > self.h[largest]:
            largest = left
        if right is not None and self.h[right] > self.h[largest]:
            largest = right
        if largest != i:
            self.h[i], self.h[largest] = self.h[largest], self.h[i]
            self._max_heapify(largest)
    def build_heap(self, a):
        self.currsize = len(a)
        self.h = list(a)
        for i in range(self.currsize
            self._max_heapify(i)
    def get_max(self):
        if self.currsize >= 1:
            max_elem = self.h[0]
            self.h[0], self.h[self.currsize - 1] = self.h[self.currsize - 1], self.h[0]
            self.currsize -= 1
            self._max_heapify(0)
            return max_elem
        return None
    def heap_sort(self):
        size = self.currsize
        for i in range(self.currsize - 1, 0, -1):
            self.h[0], self.h[i] = self.h[i], self.h[0]
            self.currsize -= 1
            self._max_heapify(0)
        self.currsize = size
    def insert(self, data):
        self.h.append(data)
        self.currsize += 1
        current = self.currsize - 1
        parent = (current - 1)
        while current > 0 and self.h[current] > self.h[parent]:
            self.h[current], self.h[parent] = self.h[parent], self.h[current]
            current = parent
            parent = (current - 1)
    def display(self):
        print(self.h)
def main():
    print("=== Heap (max) - A specialized tree-based data structure that satisfies the max-heap property.")
    sentence = input("[STR] What is your sentence? ").split()
    heap = Heap()
    heap.build_heap(sentence)
    heap.heap_sort()
    heap.display()
if __name__ == '__main__':
    main()